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
from django.conf.urls import url, include
from django.contrib import admin
from run import views as core_views

from run import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', core_views.signup, name='signup'),
    url('', include('social_django.urls', namespace='social')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^api/trainings$', views.TrainingsViewAPI.as_view(), name='trainings'),
    url(r'^api/training/(?P<id>(\d)+)$', views.TrainingViewAPI.as_view(), name='training-api'),
    url(r'^api/users$', views.PeopleViewAPI.as_view(), name='users'),
    url(r'^api/users/(?P<pk>(\d)+)$', views.PersonViewAPI.as_view(), name='user'),
    url(r'^training/(?P<training_id>(\d)+)$', views.TrainingView.as_view(), name='training-details'),
    url(r'^add-training$', views.AddTrainingView.as_view(), name='add-training'),
    url(r'^training/(?P<training_id>\d+)/comment/$', views.add_comment_to_training, name='add_comment_to_training'),

]
