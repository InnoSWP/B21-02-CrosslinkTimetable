from django.test import SimpleTestCase
from django.urls import reverse, resolve
from WideEvents.views import create_event, EventAPIView, profile

class TestUrls(SimpleTestCase):
    def test_createevent_url_is_resolved(self):
        url = reverse('create-event')
        self.assertEqual(resolve(url).func, create_event)
    
    def test_welcome_url_is_resolved(self):
        url = reverse('welcome') 
        self.assertEqual(resolve(url).func.view_class, EventAPIView)
    
    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)
