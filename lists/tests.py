from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
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

    def test_home_page_returns_correct_html(self):
        request=HttpRequest()
        #we emit a request from client
        response=home_page(request)
        #here we get response from server/home_page
        html=response.content.decode('utf8')
        #here we get a html content string to send to client
        self.assertTrue(html.startswith('<html>'))
        #test whether the content has <html>
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))

