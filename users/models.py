from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from materials.models import Course, Lesson

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(max_length=16, verbose_name="Номер телефона", blank=True, null=True)
    city = models.CharField(max_length=111, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", verbose_name="Аватар", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    CASH = "cash"
    TRANSFER = "transfer"

    PAY_METHOD_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, verbose_name="Оплаченный курс", blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name="Оплаченный урок", blank=True, null=True)
    pay_method = models.CharField(max_length=10, choices=PAY_METHOD_CHOICES, default=CASH, verbose_name="Способ оплаты")
    session_id = models.CharField(max_length=500, blank=True, null=True, verbose_name="ID сессии")
    link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Ссылка на оплату")

    def __str__(self):
        return f"{self.user.email}"

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"
