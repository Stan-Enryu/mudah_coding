from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.course_view, name='browse'),
    path('<str:course_slug>', views.step_course, name='step_course'),
    path('<str:course_slug>/<str:step_slug>/<int:sub_step_id>/', views.sub_step_course, name='sub_step_course'),
    path('<str:course_slug>/review/view',views.review_view, name='review-view'),
    path('<str:course_slug>/review/create',views.review_create, name='review-create'),
]