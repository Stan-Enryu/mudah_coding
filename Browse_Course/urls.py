from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.List_All_Course_View, name='browse'),
    path('<str:course_slug>', views.Detail_Step_Course_View, name='step_course'),
    path('<str:course_slug>/<str:step_slug>/<int:sub_step_id>/', views.Do_Sub_Step_Course, name='sub_step_course'),
    path('<str:course_slug>/review/view',views.Review_View, name='review-view'),
    path('<str:course_slug>/review/create',views.Review_Create, name='review-create'),
]