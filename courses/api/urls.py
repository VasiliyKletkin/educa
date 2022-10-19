from django.urls import include
from django.urls import re_path as url
from rest_framework import routers

from . import views

app_name = 'courses'


router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    url(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'),
    url(r'^subjects/(?P<pk>\d+)/$',
        views.SubjectDetailView.as_view(), name='subject_detail'),
    url(r'^', include(router.urls)),

]
