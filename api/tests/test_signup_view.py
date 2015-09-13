from django.core.urlresolvers import reverse
from django.test import TestCase
from api.tests.mixins import NewUserFixtureMixin


class TestSignupView(NewUserFixtureMixin, TestCase):
    view_name = 'signup_view'
    url = reverse(view_name)

    def test_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        data = {
            'username': 'new_user',
            'password': self.user.password,
            'confirm_password': self.user.password
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_bad_signup(self):
        data = {
            'username': '',
            'password': self.user.password,
            'confirm_password': self.user.password
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
