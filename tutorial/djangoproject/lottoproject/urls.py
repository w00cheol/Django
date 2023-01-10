"""lottoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from apps.lottoapp import views as lottoviews

urlpatterns = [
    re_path(r'^$', lottoviews.index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^lotto/$', lottoviews.index, name='read_lotto'),
    re_path(r'^lotto/new/$', lottoviews.post, name='create_lotto'),
    re_path(r'^lotto/(?P<lottokey>[0-9]+)/$', lottoviews.detail, name='detail_lotto'),
]
