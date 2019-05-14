from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView, UpdateView
from rest_framework import viewsets

from wykop.accounts.forms import ConfirmTosForm, RegisterForm
from wykop.accounts.models import User
from wykop.accounts.serializers import UserSerializer
from wykop.settings import CURRENT_TOS_VERSION


class LogoutRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse(settings.LOGIN_REDIRECT_URL))
        return super().dispatch(request, *args, **kwargs)


class RegisterView(LogoutRequiredMixin, FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('posts:list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserLoginView(LogoutRequiredMixin, LoginView):
    template_name = 'login.html'


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'profile'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user_update.html'
    fields = ('first_name', 'last_name', 'email')

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse(
            'accounts:profile',
            args=(self.request.user.pk, )
        )


class ConfirmTosView(LoginRequiredMixin, FormView):
    template_name = 'confirm_tos.html'
    form_class = ConfirmTosForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['tos_version'] = settings.CURRENT_TOS_VERSION
        return ctx

    def form_valid(self, form):
        user = self.request.user
        user.accepted_tos = settings.CURRENT_TOS_VERSION
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return next
        return reverse('posts:list')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
