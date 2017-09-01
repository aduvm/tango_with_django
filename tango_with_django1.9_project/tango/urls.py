from django.conf.urls import url
from tango import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$',views.about,name='about'),
    url(r'^category/(?P<category_id>\d+)/$',views.show_category,name='show_category'),
    url(r'^page/(?P<page_id>\d+)/$',views.show_page,name='show_page'),
    url(r'^add_category/$',views.add_category,name='add_category'),
    url(r'^add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]