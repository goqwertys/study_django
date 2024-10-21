from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone_number = PhoneNumberField(
        verbose_name='phone_number',
        null=True,
        blank=True,
        help_text='Enter your phone number')
    avatar = models.ImageField(
        upload_to='users/avatars',
        verbose_name='avatar',
        blank=True,
        null=True,
        help_text='Upload your avatar'
    )
    country = CountryField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email.__str__()
