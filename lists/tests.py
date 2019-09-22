from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
#views aims to handle url

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        #here we resolve the url
        found=resolve('/')
        #resolve the root /
        self.assertEqual(found.func,home_page)
        #here we check after the resolvation wheather we could direct to "view" home_page




