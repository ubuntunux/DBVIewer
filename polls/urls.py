from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.add_question, name='add_question'),
    url(r'^viewimg/$', views.view_image, name='view_image'),
    url(r'^myview/$', views.myview, name='myview'),
    url(r'^list/$', views.listing, name='listing'),
    url(r'^layout/$', views.layout, name='layout'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]