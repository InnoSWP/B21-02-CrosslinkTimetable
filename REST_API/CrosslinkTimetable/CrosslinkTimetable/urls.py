"""CrosslinkTimetable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from WideEvents.views import EventAPIView, test_base_page, create_event, profile, events, signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('WideEvents', EventAPIView.as_view()),
    path('WideEvents/base', test_base_page, name="base"),
    path('WideEvents/create-event', create_event, name="create-event"),
    path('WideEvents/profile', profile, name="profile"),
    path('WideEvents/events', events, name="events"),
    
    path('WideEvents/signin', signin, name="signin"),
]
