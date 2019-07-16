from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.asserEqual(found.func, home_page)

    def test_home_page_returs_correct_html(self):
        response = self.client.get('/')

        #request = HttpRequest()
        #response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<titleTo-Do lists</title>', html)
        self.assertTrue(html.strip().endswitch('</html>'))
        #expected.html = render_to_string('home.html')
        #self.asserEqual(html, expected_html)
        self.assertTemplateUsed(response, 'home.html')

class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1 + 1, 3)
