from django.contrib import admin
from django.urls import path
from custom_user_tags_app.views import (UserListView,
                                        UserDetailView,
                                        UserCreateView,
                                        UserUpdateView,
                                        UserDeleteView,
                                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UserListView.as_view(), name='users-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-details'),
    path('users/add', UserCreateView.as_view(), name='user-add'),
    path('users/edit/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:pk>', UserDeleteView.as_view(), name='user-delete'),
]
