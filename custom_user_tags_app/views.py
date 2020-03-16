from django.http import FileResponse, HttpResponse
from django.urls import reverse_lazy
from django.forms import DateInput
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from .models import User
from .utils import create_csv_file
from custom_user_tags.settings import BASE_DIR
from os import path


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


def download_csv(request):
    users = User.objects.all()
    create_csv_file(users)
    file_path = path.join(BASE_DIR, 'custom_user_tags_app/static/csv/users.csv')
    return FileResponse(open(file_path, 'rb'), filename='users.csv', as_attachment=True)
