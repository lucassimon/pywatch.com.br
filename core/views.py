# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
# Third-party app imports
from allauth.account.views import (
    RedirectAuthenticatedUserMixin,
    CloseableSignupMixin,
    AjaxCapableProcessFormViewMixin,
)
from allauth.account.utils import (
    get_next_redirect_url,
    complete_signup,
    passthrough_next_redirect_url
)

from allauth.account import app_settings

# Imports from your apps
from speakers.models import SpeakerUser
from talks.models import Talk
from .forms import CustomSignupForm


class IndexHomePageTemplateView(TemplateView):
    """
    Classe generica para renderizar o template
    da index
    """

    template_name = "index.html"
    """
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        """
        Seta objetos para o contexto
        """
        context = super(
            IndexHomePageTemplateView, self
        ).get_context_data(**kwargs)
        context['most_recent_speakers_list'] = (
            SpeakerUser.objects.latest_with_limits(5)
        )
        context['most_recent_talks_list'] = (
            Talk.objects.latest_with_limits(5)
        )
        return context


class CustomRegisterCreateView(
    RedirectAuthenticatedUserMixin,
    CloseableSignupMixin,
    AjaxCapableProcessFormViewMixin,
    FormView
):
    u"""
    Cria a view para registrar um novo usuario
    com os campos first name e last name
    """
    template_name = "account/signup.html"
    form_class = CustomSignupForm
    redirect_field_name = "next"
    success_url = None

    def get_success_url(self):
        # Explicitly passed ?next= URL takes precedence
        ret = (
            get_next_redirect_url(
                self.request,
                self.redirect_field_name
            )
            or self.success_url
        )
        return ret

    def form_valid(self, form):
        user = form.save(self.request)
        return complete_signup(
            self.request,
            user,
            app_settings.EMAIL_VERIFICATION,
            self.get_success_url()
        )

    def get_context_data(self, **kwargs):
        form = kwargs['form']
        form.fields["email"].initial = self.request.session \
            .get('account_verified_email', None)
        ret = super(CustomRegisterCreateView, self).get_context_data(**kwargs)
        login_url = passthrough_next_redirect_url(
            self.request,
            reverse("account_login"),
            self.redirect_field_name
        )
        redirect_field_name = self.redirect_field_name
        redirect_field_value = self.request.REQUEST.get(redirect_field_name)
        ret.update(
            {
                "login_url": login_url,
                "redirect_field_name": redirect_field_name,
                "redirect_field_value": redirect_field_value
            }
        )
        return ret
