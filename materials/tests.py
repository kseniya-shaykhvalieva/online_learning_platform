from django.db.models.expressions import result
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from materials.models import Lesson, Course, Subscription
from users.models import CustomUser


class LessonCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(name="Испанский язык", owner=self.user)
        self.lesson = Lesson.objects.create(name="Неправильные глаголы", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson-detail", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse("materials:lesson-create")
        data = {
            "name":"Испанский алфавит",
            "course":self.course.pk,
            "owner":self.user.pk,
            "url_video":""
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse("materials:lesson-update", args=(self.lesson.pk,))
        data = {
            "name":"Испанский алфавит",
            "course":self.course.pk,
            "owner":self.user.pk,
            "url_video":""
        }
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get("name"), "Испанский алфавит"
        )

    def test_lesson_delete(self):
        url = reverse("materials:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse("materials:lesson-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": None,
                    "preview": None,
                    "url_video": None,
                    "course": self.course.pk,
                    "owner": self.user.pk
                }
            ]
        }

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )


class SubscriptionCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="admin@mail.ru")
        self.course = Course.objects.create(name="Испанский язык", owner=self.user)
        # self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_is_subscribed(self):
        url = reverse("materials:subscription")
        data = {
            "id":self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        result = {
            "message": "Подписка добавлена"
        }
        # result = {
        #     "message": "Подписка удалена"
        # }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )
