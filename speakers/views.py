# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join
# Third-party app imports
from rest_framework import generics
from allauth.account.forms import ChangePasswordForm
# Imports from your apps
from core.views import AjaxableResponseMixin
from .models import SpeakerUser, KindContact
from .serializers import SpeakerSerializer
from .forms import (
    SpeakerBasicInformationForm,
    SpeakerContactForm
)


class SpeakerList(generics.ListCreateAPIView):
    """
    Endpoint que representa a lista de palestrantes, e permite que novos
    palestrantes sejam cadastrados.
    """
    model = SpeakerUser
    serializer_class = SpeakerSerializer


class SpeakerDetail(generics.RetrieveUpdateAPIView):
    '''
    Endpoint que representa uma instancia de palestrante, e permite que novos
    palestrantes sejam atualizados.
    '''
    model = SpeakerUser
    serializer_class = SpeakerSerializer


class SpeakerProfileTemplateView(TemplateView):
    u"""
    Classe generica para renderizar o template
    da index de palestras no dashboard
    """

    template_name = "profile.html"
    u"""
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        u"""
        Seta váriaveis para o contexto
        """
        context = super(SpeakerProfileTemplateView, self).get_context_data(
            **kwargs
        )
        context['basic_information_form'] = SpeakerBasicInformationForm(
            instance=self.request.user
        )
        context['contact_list'] = KindContact.objects.filter(
            speaker=self.request.user
        )

        context['password_form'] = ChangePasswordForm(
            user=self.request.user
        )

        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(SpeakerProfileTemplateView, self).dispatch(
            *args,
            **kwargs
        )


class SpeakerListView(ListView):
    """
    Classe responsavel por gerar uma lista
    paginada com os palestrantes cadastrados
    no sistema.
    """

    model = SpeakerUser
    """
    Define o model a ser atribuido
    """

    template_name = "speaker_list.html"
    """
    Define o nome do template a ser utilizado
    """

    context_object_name = "speaker_list"
    """
    Define o nome do objeto a ser renderizado
    no contexto da requisição
    """

    paginate_by = 10
    """
    Define o tamanho dos items a serem
    paginados
    """

    def get_queryset(self, *args, **kwargs):
        """
        Personaliza o queryset dos palestrantes
        resgatando o contatos caso existam
        """

        qs = super(SpeakerListView, self).get_queryset(*args, **kwargs)
        qs = qs.no_superusers()
        qs = (
            qs.order_by('first_name')
            .exclude(username='root')
        )

        sw = self.request.GET.get('letter', None)
        if sw:
            return qs.filter(first_name__istartswith=sw)

        if qs:
            return qs
        else:
            return []

    def get_context_data(self, **kwargs):
        """
        Envia ao contexto os dados personalizados
        """
        context = super(SpeakerListView, self).get_context_data(
            **kwargs
        )

        speakers = filter(
            None,
            SpeakerUser.objects.no_superusers().values_list(
                'first_name',
                flat=True
            )
        )

        letters = [x[0] for x in speakers]
        letters = set(letters)
        new_letters = list(letters)
        context['letters'] = new_letters

        del letters
        del new_letters
        return context


class SpeakerDetailView(DetailView):
    """
    Classe responsavel por gerar o detalhe
    da palestra
    """

    model = SpeakerUser
    """
    Define o model a ser atribuido
    """

    template_name = "speaker_detail.html"
    """
    Define o nome do template a ser utilizado
    """

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        return context


class SpeakerBasicInformationProfile(AjaxableResponseMixin, CreateView):
    model = SpeakerUser
    fields = ['id', 'first_name', 'last_name', 'bio']

    def get_object(self, queryset=None, pk=None):

        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with "
                "either an object pk or a slug."
                % self.__class__.__name__
            )

        if queryset is None:
            queryset = self.get_queryset()

        if pk is not None:
            queryset = queryset.filter(pk=pk)

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _("No %(verbose_name)s found matching the query") %
                {'verbose_name': queryset.model._meta.verbose_name}
            )
        return obj

    def form_valid(self, form):
        if self.request.is_ajax():

            obj = self.get_object(
                pk=self.request.POST.get('pk', None)
            )

            form = SpeakerBasicInformationForm(
                self.request.POST,
                instance=obj
            )
            if form.is_valid():
                form.save()
                data = {
                    'success': True,
                    'message': _(u'Dados salvos com sucesso')
                }
            else:
                data = {
                    'success': False,
                    'errors': self.build_errors_as_ul(
                        form.errors
                    )
                }
            return JsonResponse(data)
        else:
            response = super(AjaxableResponseMixin, self).form_valid(form)

            return response

    def build_errors_as_ul(self, errors):
        """
        """

        items = []
        for v in errors.values():
            for i in v:
                items.append(u'<li>{}</li>'.format(i))

        msg = ''.join(v for v in items)
        return u'<ul>{}</ul>'.format(
            msg
        )


class KindContactCreateView(CreateView):
    """
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/kindcontacts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = SpeakerContactForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('speakers:speaker-profile-view')
    """
    Define a url de sucesso apos criar o objeto de video
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(KindContactCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        u"""
        Seta as variaveis do formset para o cotexto do formulário
        """
        context = super(KindContactCreateView, self).get_context_data(
            **kwargs
        )
        return context

    def form_valid(self, form):
        u"""
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        contact = form.save(commit=False)
        # seta o commit do formulario como false

        contact.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado
        contact.save()
        super(KindContactCreateView, self).form_valid(form)
        # chama o metodo super

        # e retorna para a página de sucesso
        return HttpResponseRedirect(
            self.get_success_url()
        )

    def get_form_kwargs(self):
        u"""
        Retorna o usuário corrente para o formulario
        """
        kwargs = super(KindContactCreateView, self).get_form_kwargs()
        return kwargs


class KindContactUpdateView(UpdateView):
    """
    Classe generica para criar as videos
    do usuário
    """
    template_name = "dashboards/kindcontacts/create.html"
    """
    Define o nome do template a ser utilizado
    """

    form_class = SpeakerContactForm
    """
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('speakers:speaker-profile-view')
    """
    Define a url de sucesso apos criar o objeto de video
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(KindContactUpdateView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a video
        de acordo com o id dela
        """
        obj = KindContact.objects.get(id=self.kwargs['pk'])
        return obj

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', None)
        if pk is not None:
            contact = KindContact.objects.get(pk=pk)
        else:
            raise AttributeError(
                _(u"Não conseguimos localizar este contato %s" % pk)
            )

        form = SpeakerContactForm(request.POST, instance=contact)

        if form.is_valid():
            self.form_valid(form)
            # e retorna para a página de sucesso
            return HttpResponseRedirect(
                self.get_success_url()
            )
        else:
            self.form_invalid(form)
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        u"""
        Sobrescreve o metodo form_valid para buscar
        o palestrante/user através do request
        """
        contact = form.save(commit=False)
        # seta o commit do formulario como false

        contact.speaker = SpeakerUser.objects.get(
            username=self.request.user.username
        )
        # associa o palestrante de acordo
        # com uma pesquisa feito no model SpeakerUser
        # filtrando pelo usuario logado

        contact.save()
        # salvar a o formulario

        super(KindContactUpdateView, self).form_valid(form)
        # chama o metodo super

    def form_invalid(self, form):
        u"""
        Sobrescreve o metodo form_invalid para o contexto
        com o formulario preenchido
        """
        super(KindContactUpdateView, self).form_invalid(form)


class KindContactDeleteView(DeleteView):
    u"""
    Classe generica para deletar os contatos do palestrante
    """
    template_name = "dashboards/kindcontacts/delete.html"
    u"""
    Define o nome do template a ser utilizado
    """

    model = KindContact
    u"""
    Define o formulario a ser renderizado no template
    """

    success_url = reverse_lazy('speakers:speaker-profile-view')
    u"""
    Define a url de sucesso apos deletar o objeto
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        u"""
        To decorate every instance of a class-based view,
        you need to decorate the class definition itself.
        To do this you apply the decorator to the dispatch()
        method of the class.
        """
        return super(KindContactDeleteView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        """
        Sobrescreve o metodo para buscar a video
        de acordo com o id dela
        """
        obj = KindContact.objects.get(id=self.kwargs['pk'])
        return obj
