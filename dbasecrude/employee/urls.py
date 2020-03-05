from django.conf.urls import url, include
from .import views


urlpatterns = [
    url('^$', views.emp),
    url('show/',views.show),
    url('edit/(?P<id>[\d]*)/',views.edit),
    url('update/(?P<id>[\d]*)/',views.update),
    url('delete/(?P<id>[\d]*)/', views.destroy),
]
