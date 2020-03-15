from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  )
from .models import User


class UserListView(ListView):
    model = User
    paginate_by = 50
    template_name = "custom_user_tags_app/user-list.html"
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User
