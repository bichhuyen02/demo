from django.views import View
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, status, parsers
from rest_framework.decorators import action
from django.shortcuts import render

from . import serializers
from .models import Course, User, Lesson, Tag, Category
from .serializers import CourseSerializer, LessonSerializer, TagSerializer, CategorySerializer, UserSerializer
from .paginator import CoursePaginator


def index(request):
    return HttpResponse("e-Course App")


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CoursePaginator


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def lessons(self, request, pk):
        l = self.get_object().lesson_set.all()
        return Response(LessonSerializer(l, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_name='current_user', detail=False)
    def current_user(self, requets):
        return Response(serializers.CourseSerializer().data)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePaginator


class TagViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Tag.objects.filter(active=True)
    serializer_class = TagSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CoursePaginator


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = UserSerializer
    parsers_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_name='current_user', detail=False)
    def current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)


class CategoryView(View):
    pass
