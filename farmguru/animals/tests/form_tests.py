from django.test import TestCase
from animals.forms import AnimalForm
from animals.models import Animal


class AnimalFormTestCase(TestCase):
    def test_valid_form(self):
        # Only required fields are identity and gender
        form = AnimalForm({
            'animal_id': '101',
            'gender': Animal.GENDER_CHOICES.bull
        })
        self.assertTrue(form.is_valid())
        animal = form.save()
        self.assertEqual(animal.animal_id, '101')
        self.assertEqual(animal.gender, Animal.GENDER_CHOICES.bull)

    def test_invalid_form(self):
        # Identity and gender are missing
        form = AnimalForm({})
        self.assertEqual(form.errors,
                         {'gender': [u'This field is required.'], '__all__': [u'Some kind of identification is required']})
