from django.contrib import admin
from django.urls import path
from WideEvents.views import EventAPIView, test_base_page, create_event, profile, events, calendar, loginPage, sendEmail
from WideEvents.views import registerPage
from DoE_emails.views import DoEEmailsAPIView
from Auth.views import AuthAPIView

urlpatterns = [
    path('', loginPage, name="login"),
    path('login/auth', AuthAPIView.as_view(), name='auth'),
    path('admin/', admin.site.urls, name="admin"),
    path('WideEvents', EventAPIView.as_view(), name="WideEvents"),
    path('DoE', DoEEmailsAPIView.as_view(), name="DoE"),
    path('DoE/sendEmail', sendEmail, name="sendEmail"),
    path('WideEvents/base', test_base_page, name="base"),
    path('WideEvents/create-event', create_event, name="create-event"),
    path('WideEvents/profile', profile, name="profile"),
    path('WideEvents/events', events, name="events"),
    # path('WideEvents/signin', signin, name="signin"),
    path('login/', loginPage, name="login"),
    path('register/', registerPage, name="register"),
    path('WideEvents/calendar', calendar, name="calendar")
]
