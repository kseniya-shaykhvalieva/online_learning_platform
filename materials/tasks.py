from celery import shared_task
from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL
from materials.models import Subscription


@shared_task
def mailing_for_updates(course_id):
    email_list = []
    subscriptions = Subscription.objects.filter(course_id=course_id)
    for sub in subscriptions:
        email_list.append(sub.user.email)
    if email_list:
        send_mail(
            subject="Обновление курса",
            message="Здравствуйте! Курс, на который вы подписаны, обновлен. Зайдите на сайт и посмотрите изменения.",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=email_list,
        )
