from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from random import randint


def get_random_number():
    return randint(1, 100)


class User(AbstractUser):
    birthday = models.DateField()
    random_number = models.IntegerField(default=get_random_number)

    @property
    def age(self):
        today = date.today()
        delta_days = (today - self.birthday).days
        return int(delta_days / 365.242199)
