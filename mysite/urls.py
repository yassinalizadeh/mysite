"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.contrib.auth import views

urlpatterns = [
    # todo why not path('', include(' blog.urls')),
    url(r'', include('blog.urls')),
    path('admin/', admin.site.urls),
    # todo LoginView.as_view()!!!
    # todo where login is used?
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    # todo where logout and next_page and '/' is used?
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]


