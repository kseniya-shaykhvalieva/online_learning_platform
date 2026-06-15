from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons_list = LessonSerializer(many=True)

    def get_lessons_count(self, obj):
        return obj.lessons.all().count()

    class Meta:
        model = Course
        fields = '__all__'
