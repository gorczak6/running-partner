"""rp URL Configuration

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

from run import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^trenings/$', views.TreningsView.as_view(), name='trenings'),
    # url(r'^add-trening/$', views.AddTreningView.as_view(), name='add-trening'),
    url(r'^trening/(?P<id>(\d)+)', views.TreningView.as_view(), name='trening'),
    url(r'^users/$', views.PeopleView.as_view(), name='users'),
    url(r'^users/(?P<pk>(\d)+)', views.PersonView.as_view(), name='user'),
]
