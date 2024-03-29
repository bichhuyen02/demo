from rest_framework import serializers
from .models import Course, User, Lesson, Tag, Category


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)
    category = CategorySerializer()

    def get_image(self, obj):
        request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = '/static/%s' % (obj.image)

        return request.build_absolute_uri(path)

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    # tags = TagSerializer(many=True)

    def get_image(self, obj):
        request = self.context['request']
        if obj.image.name.startswith('static/'):
            path = "/%s" % obj.image.name
        else:
            path = '/static/%s' % (obj.image)

        return request.build_absolute_uri(path)

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date', 'course_id']


class UserSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField(source='image')

    # def get_image(self, obj):
    #     request = self.context['request']
    #     if obj.image.name.startswith('static/'):
    #         path = "/%s" % obj.image.name
    #     else:
    #         path = '/static/%s' % (obj.image)
    #
    #     return request.build_absolute_uri(path)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email',  'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data['password'] )
        user.save()
        return user