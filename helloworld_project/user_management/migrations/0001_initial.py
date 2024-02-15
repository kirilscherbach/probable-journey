# Generated by Django 4.2.5 on 2024-02-15 21:38

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, User
from django.db import migrations


def generate_superuser(apps, schema_editor):
    email = settings.DJANGO_SUPERUSER_EMAIL
    password = settings.DJANGO_SUPERUSER_PASSWORD
    username = settings.DJANGO_SUPERUSER_USERNAME

    user = User()
    user.pk = 1
    user.email = BaseUserManager.normalize_email(email)
    user.password = make_password(password)
    user.username = username
    user.is_staff = True
    user.is_superuser = True
    user.save()


def drop_superuser(apps, schema_editor):
    User.objects.filter(pk=1).delete()


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(generate_superuser, drop_superuser),
    ]
