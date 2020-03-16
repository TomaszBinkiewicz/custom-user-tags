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

    def save(self, *args, **kwargs):
        super(User, self).save(self, *args, **kwargs)
        self.random_number = randint(1, 100)
