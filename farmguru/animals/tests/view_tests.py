from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission
from animals.models import Animal
from helpers import test_helpers


class AnimalCRUDLTestCase(TestCase):
    def test_creating_animal(self):
        user = test_helpers.create_logged_in_user(self)
        user.user_permissions.add(Permission.objects.get(codename='animal_create'))
        user.user_permissions.add(Permission.objects.get(codename='animal_list'))
        post_data = {
            'animal_id': '101',
            'gender': Animal.GENDER_CHOICES.bull
        }
        url = reverse('animals.animal_create')
        response = self.client.post(url, post_data, follow=True)
        self.assertContains(response, 'Your new animal has been created.')
