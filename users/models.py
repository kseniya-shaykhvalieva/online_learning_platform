from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(max_length=16, verbose_name="Номер телефона", blank=True, null=True)
    city = models.CharField(max_length=111, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", verbose_name="Аватар", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
