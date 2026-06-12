from django.db import models


class Course(models.Model):
    """Курс"""

    name = models.CharField(max_length=100, verbose_name="Название", help_text="Введите название курса")
    preview = models.ImageField(
        upload_to="image_course/", verbose_name="Превью", help_text="Загрузите изображение", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", help_text="Введите описание курса", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    """Урок"""

    name = models.CharField(max_length=200, verbose_name="Название", help_text="Введите название урока")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание урока", blank=True, null=True)
    preview = models.ImageField(
        upload_to="image_lesson/", verbose_name="Превью", help_text="Загрузите изображение", blank=True, null=True
    )
    url_video = models.TextField(
        verbose_name="Ссылка на видео", help_text="Вставьте ссылку на видео", blank=True, null=True
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс", help_text="Выберете курс")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
