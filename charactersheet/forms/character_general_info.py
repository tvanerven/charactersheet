from charactersheet.models.character_general_info import GeneralCharacterInfo
from django.forms import ModelForm


class GeneralCharacterInfoForm(ModelForm):

    class Meta:
        model = GeneralCharacterInfo

        fields = [
            'name',
            'alignment',
            'player',
            'level',
            'race',
            'classes',
            'gender',
            'eye_color',
            'hair_color',
            'size',
            'height',
            'weight',
            'deity',
            'homeland',
        ]
