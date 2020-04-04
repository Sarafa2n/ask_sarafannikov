from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import re
from django.core.files.images import get_image_dimensions
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator, FileExtensionValidator

from .models import Profile


def validate_nickname(value):
    if Profile.objects.filter(nickname__iexact=value).exists():
        raise ValidationError('A user with this nickname already exists.')


def validate_email(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('A user with this email already exists.')


def validate_username(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('A user with this login already exists.')


