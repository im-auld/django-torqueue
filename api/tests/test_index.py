from django.core.urlresolvers import reverse
from django.test import TestCase
from factories import UserFactory
from mixins import UserFixtureMixin

class TestIndexView(UserFixtureMixin, TestCase):
    view_name = 'index'
    url = reverse(view_name)

    def test_anonymous_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        data = {
            'username': self.user.username,
            'password': 'password'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_invlaid_login(self):
        data = {
            'username': self.user.username,
            'password': 'somestring'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
