from charactersheet.models.character_base_statistics import CharacterBaseStatistics
from django.forms import ModelForm

class CharacterBaseStatisticsForm(ModelForm):

    class Meta:
        model = CharacterBaseStatistics

        fields = [
            'strength',
            'dexterity',
            'constituation',
            'intelligence',
            'wisdom',
            'charisma',
        ]
