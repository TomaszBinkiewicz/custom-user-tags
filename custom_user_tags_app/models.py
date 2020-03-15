from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from random import randint


class User(AbstractUser):
    birthday = models.DateField()
    random_number = models.IntegerField()

    @property
    def age(self):
        today = date.today()
        delta_days = (today - self.birthday).days
        return int(delta_days / 365.242199)

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
        self.random_number = randint(1, 100)
