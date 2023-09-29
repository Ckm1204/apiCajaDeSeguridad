from django.db import models
from django import forms
from django.utils import timezone

class MonthYearField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7  # MM/YYYY has a length of 7
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        return value

    def get_prep_value(self, value):
        return value

    def formfield(self, **kwargs):
        kwargs['widget'] = forms.TextInput(attrs={'placeholder': 'MM/YYYY'})
        return super().formfield(**kwargs)

# Create your models here.

class Secret(models.Model):
    name = models.CharField(max_length=50)
    secret = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)


class Identification(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    fullName = models.CharField(max_length=80)
    birthDate = models.DateField()
    expeditionDate = models.DateField()
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)



class loginKey(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)



class card(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=30)
    expirationDate = MonthYearField()
    cvv = models.CharField(max_length=3)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
