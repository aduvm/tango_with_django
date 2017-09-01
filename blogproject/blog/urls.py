from django.conf.urls import url
from blog import views
urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^about$', views.about,name='about'),
    url(r'^contact$', views.contact,name='contact'),
    url(r'^full_width$', views.full_width,name = 'full_width'),
    url(r'^post/(?P<pk>[0-9]+)$', views.detail,name = 'detail'),
]