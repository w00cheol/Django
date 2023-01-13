from django.urls import path, re_path
from . import views

app_name = 'vote'

urlpatterns = [
    # Class-based View

    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), # 매개변수 이름을 pk 로
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'), # 매개변수 이름을 pk 로
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    # Function-based View

    # re_path(r'^$', views.index, name='index'),
    # re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]