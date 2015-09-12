from django.core.urlresolvers import reverse
from django.test import TestCase
from api.tests.mixins import CharacterFixtureMixin


class TestAddCharacterView(CharacterFixtureMixin, TestCase):
    view_name = 'add_character_view'
    url = reverse(view_name)

    def test_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index') + '?next=/add-character/')

    def test_logged_in(self):
        logged_in = self.client.login(username=self.user.username, password='password')
        self.assertTrue(logged_in)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_character_logged_in(self):
        logged_in = self.client.login(username=self.user.username, password='password')
        self.assertTrue(logged_in)
        data = {
            'name': self.character.name,
            'adv_class': self.character.adv_class,
            'server': self.server.pk
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_create_character_no_login(self):
        data = {
            'name': self.character.name,
            'adv_class': self.character.adv_class,
            'server': self.server.pk
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index') + '?next=/add-character/')

