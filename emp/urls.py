from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /emp/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<emp_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^success/$', views.success, name='success'),
    url(r'^overwrite/$', views.overwrite, name='overwrite'),
    url(r'^upload_file/$', views.upload_file, name='upload_file')
]
