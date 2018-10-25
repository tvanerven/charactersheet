from django.test import TestCase
from charactersheet.models.choices import (
    AlignmentChoices,
    RaceChoices,
    ClassChoices,
    GenderChoices,
    SizeChoices,
)
from charactersheet.models.character_general_info import GeneralCharacterInfo


class FormSavingTestCase(TestCase):

    def test_form_saves_to_database(self):
        data = {
            'name': 'Testname',
            'age': '29',
            'classes': ClassChoices.CLERIC,
            'gender': GenderChoices.MALE,
            'size': SizeChoices.MEDIUM,
            'eye_color': 'Blue',
            'hair_color': 'Brown',
            'height': '178',
            'weight': '85',
            'race': RaceChoices.HUMAN,
            'level': '24',
            'alignment': AlignmentChoices.LN
        }
        url = '/charactersheet/new/'
        response = self.client.post(url, data=data)
        character = GeneralCharacterInfo.objects.last()
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertEqual(
            character.name,
            data['name']
        )
