from django.urls import path
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe

from .dao import count_course_by_cat
from .models import Category, Course, Lesson, Tag, User


# Register your models here.
class AppAdminSite(admin.AdminSite):
    site_header = 'Hệ thống khoá học trực tuyến'

    def get_urls(self):
        return [
            path('course-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        stats = count_course_by_cat
        return TemplateResponse(request,
                                'admin/course-stats.html', {
                                    'stats': stats
                                })


# thiết lập khóa ngoại giao diện
class CourseTagInlineAdmin(admin.TabularInline):
    model = Course.tags.through


class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tags.through


# form RichTextField
class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class LessonForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    search_fields = ['subject']
    list_filter = ['id', 'subject']
    form = CourseForm
    inlines = [CourseTagInlineAdmin]
    readonly_fields = ['ava']

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }

    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description']
    form = LessonForm
    inlines = [LessonTagInlineAdmin]
    readonly_fields = ['ava']

    def ava(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


class TagAdmin(admin.ModelAdmin):
    pass


admin_site = AppAdminSite(name='myadmin')

admin_site.register(Category, CategoryAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
admin_site.register(Tag)
admin_site.register(User)
