from django.contrib import admin
from django.urls import path
from custom_user_tags_app.views import (UserListView,
                                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users', UserListView.as_view(), name='users-list'),
]
