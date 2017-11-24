"""lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lab2 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lab2/', views.lab2 , name='lab2'),
    url(r'^show', views.show),
    url(r'^delete', views.delete),
    url(r'^update', views.update),
    url(r'^confirm_update', views.confirm_update),
    url(r'^create', views.create),
    url(r'^upload', views.upload),
    url(r'^searchvarchars', views.searchvarchars),
    url(r'^searchword', views.searchword),
    url(r'^searchdigit', views.searchdigit),
]
