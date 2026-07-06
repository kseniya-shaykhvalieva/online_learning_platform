from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validations import UrlVideoValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlVideoValidator(field='url_video')]


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()
    lessons_list = LessonSerializer(many=True, source='lessons')

    def get_lessons_count(self, obj):
        return obj.lessons.all().count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=obj).exists()

    class Meta:
        model = Course
        fields = '__all__'
