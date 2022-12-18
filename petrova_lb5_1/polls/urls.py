from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path(r'^(?P<question_id>[0-9]+)/result/$', views.ResultsView.as_view(), name='results'),
    path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]


