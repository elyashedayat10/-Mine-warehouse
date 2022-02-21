from django.db import models
from django import forms
from django.conf import settings
from django.utils import timezone
User = settings.AUTH_USER_MODEL


class Hold(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pin = models.CharField(max_length=64, blank=True, null=True)
    field = models.CharField(max_length=64, blank=True, null=True)
    tonnage = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    male = models.BooleanField(default=True, blank=True, null=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to="demand/", blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"


class HoldForm(forms.ModelForm):
    class Meta:
        model = Hold
        exclude = ['user']


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=64, blank=True, null=True)
    tonnage = models.CharField(max_length=254, blank=True, null=True)
    male = models.BooleanField(default=True, blank=True, null=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    occupation = models.CharField(max_length=64, blank=True, null=True)
    company = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    visit_date = models.CharField(max_length=64, blank=True, null=True)
    visit_hour = models.CharField(max_length=64, blank=True, null=True)
    visit_minute = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to="demand/", blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        exclude = ['user']


class Sample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pin = models.CharField(max_length=64, blank=True, null=True)
    field = models.CharField(max_length=64, blank=True, null=True)
    tonnage = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    male = models.BooleanField(default=True, blank=True, null=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    file = models.FileField(upload_to="demand/", blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        exclude = ['user']
