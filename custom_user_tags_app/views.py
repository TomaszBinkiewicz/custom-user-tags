from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms import DateInput
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from .models import User


class UserListView(ListView):
    model = User
    paginate_by = 25
    template_name = "custom_user_tags_app/user-list.html"
    context_object_name = 'users'
    ordering = ['username']


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'birthday']
    template_name = 'custom_user_tags_app/user_form.html'
    success_url = reverse_lazy('users-list')

    def get_form(self, form_class=None):
        form = super(UserCreateView, self).get_form(form_class)
        form.fields['birthday'].widget = DateInput(format='%d-%m-%Y', attrs={'type': 'date'})
        return form


class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'birthday']
    template_name = 'custom_user_tags_app/user_update_form.html'
    success_url = reverse_lazy('users-list')


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users-list')
