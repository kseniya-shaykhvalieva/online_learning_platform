from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'city',)
    list_filter = ('id',)
    search_fields = ('email',)
