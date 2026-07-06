from django.utils import timezone
from celery import shared_task

from users.models import CustomUser


@shared_task
def block_inactive_users():
    today = timezone.now()
    users = CustomUser.objects.all()
    block_list = []
    for user in users:
        if user.last_login and (today-user.last_login).days > 30:
            block_list.append(user)
    if block_list:
        for user in block_list:
            user.is_active = False
            user.save()
