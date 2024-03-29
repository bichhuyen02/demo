from django.urls import path, include
from . import views

urlpatterns = [
    path('courses/', views.index, name="index"),
    path('categorise/', views.index, name="index"),
    path('categorise/<int:course_id>', views.list, name="list"),
    path('lessons/', views.index, name="index")
    # path('categorise/', views.index, name="index")
]
