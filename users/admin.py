from django.contrib import admin

from .models import CustomUser, Payment


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone",
        "city",
    )
    list_filter = ("id",)
    search_fields = ("email",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pay_date", "course", "lesson", "pay_method")
    list_filter = ("id",)
    search_fields = ("user",)
