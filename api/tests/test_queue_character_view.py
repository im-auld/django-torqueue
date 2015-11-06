from django.core.urlresolvers import reverse
from django.test import TestCase
from api.tests.mixins import QueueCharacterFixtureMixin


class TestQueueCharacterView(QueueCharacterFixtureMixin, TestCase):
    view_name = 'queue_character_view'

    def test_anonymous_user(self):
        url = reverse(self.view_name, kwargs={'character_id': self.character.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '{}{}{}'.format(reverse('index'), '?next=/queue/', self.character.pk)
        )

    def test_logged_in_user(self):
        logged_in = self.client.login(username=self.user.username, password='password')
        self.assertTrue(logged_in)
        url = reverse(self.view_name, kwargs={'character_id': self.character.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.client.logout()
