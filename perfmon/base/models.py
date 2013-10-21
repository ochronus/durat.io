""" Basic models, such as user profile """
from django.db import models
from django.contrib.auth.models import User as django_user
from django_extensions.db.fields import UUIDField
from django.forms import ModelForm

class Site(models.Model):
    name = models.CharField(max_length=128)
    domain = models.CharField(max_length=128)
    uuid = UUIDField(unique=True)
    owner = models.ForeignKey(django_user)

class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'domain']