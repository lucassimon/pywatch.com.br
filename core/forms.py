# -*- coding:utf-8 -*-

# Stdlib imports
import warnings
# Core Django imports
from django import forms
from django.utils.translation import ugettext_lazy as _, ugettext
# Third-party app imports
from allauth.account import app_settings
from allauth.account.forms import (
    _base_signup_form_class,
    email_address_exists,
    setup_user_email,
    set_form_field_order,
    PasswordField,
    SetPasswordField,

)
from allauth.account.adapter import get_adapter

# Imports from your apps


class BaseSignupForm(_base_signup_form_class()):
    username = forms.CharField(
        label=_("Username"),
        max_length=30,
        min_length=app_settings.USERNAME_MIN_LENGTH,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Username'),
                'autofocus': 'autofocus'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'placeholder': _('E-mail address')
            }
        )
    )

    first_name = forms.CharField(
        label=_("First Name"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('First Name'),
                }
        )
    )

    last_name = forms.CharField(
        label=_("Last Name"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Last Name'),
                }
        )
    )

    def __init__(self, *args, **kwargs):
        email_required = kwargs.pop(
            'email_required',
            app_settings.EMAIL_REQUIRED
        )
        self.username_required = kwargs.pop(
            'username_required',
            app_settings.USERNAME_REQUIRED
        )
        super(BaseSignupForm, self).__init__(*args, **kwargs)
        # field order may contain additional fields from our base class,
        # so take proper care when reordering...
        field_order = ['email', 'username']
        merged_field_order = list(self.fields.keys())
        if email_required:
            self.fields["email"].label = ugettext("E-mail")
            self.fields["email"].required = True
        else:
            self.fields["email"].label = ugettext("E-mail (optional)")
            self.fields["email"].required = False
            if self.username_required:
                field_order = ['username', 'email']

        # Merge our email and username fields in if they are not
        # currently in the order.  This is to allow others to
        # re-arrange email and username if they desire.  Go in reverse
        # so that we make sure the inserted items are always
        # prepended.
        for field in reversed(field_order):
            if not field in merged_field_order:
                merged_field_order.insert(0, field)
        set_form_field_order(self, merged_field_order)
        if not self.username_required:
            del self.fields["username"]

    def clean_username(self):
        value = self.cleaned_data["username"]
        value = get_adapter().clean_username(value)
        return value

    def clean_email(self):
        value = self.cleaned_data["email"]
        value = get_adapter().clean_email(value)
        if app_settings.UNIQUE_EMAIL:
            if value and email_address_exists(value):
                self.raise_duplicate_email_error()
        return value

    def raise_duplicate_email_error(self):
        raise forms.ValidationError(
            _("A user is already registered with this e-mail address.")
        )

    def custom_signup(self, request, user):
        custom_form = super(BaseSignupForm, self)
        if hasattr(custom_form, 'signup') and callable(custom_form.signup):
            custom_form.signup(request, user)
        else:
            warnings.warn(
                "The custom signup form must offer"
                " a `def signup(self, request, user)` method",
                DeprecationWarning
            )
            # Historically, it was called .save, but this is confusing
            # in case of ModelForm
            custom_form.save(user)


class CustomSignupForm(BaseSignupForm):

    password1 = SetPasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))
    confirmation_key = forms.CharField(
        max_length=40,
        required=False,
        widget=forms.HiddenInput()
    )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        if not app_settings.SIGNUP_PASSWORD_VERIFICATION:
            del self.fields["password2"]

    def clean(self):
        super(CustomSignupForm, self).clean()
        if app_settings.SIGNUP_PASSWORD_VERIFICATION \
                and "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                raise forms.ValidationError(
                    _("You must type the same password each time.")
                )
        return self.cleaned_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # TODO: Move into adapter `save_user` ?
        setup_user_email(request, user, [])
        return user
