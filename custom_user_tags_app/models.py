from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    birthday = models.DateField()

    @property
    def age(self):
        today = date.today()
        delta_days = (today - self.birthday).days
        return int(delta_days / 365.242199)
