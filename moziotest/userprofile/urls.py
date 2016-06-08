from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^service_area/$', views.ServiceAreaList.as_view()),
    url(r'^service_area/(?P<pk>[0-9]+)/$', views.ServiceAreaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
