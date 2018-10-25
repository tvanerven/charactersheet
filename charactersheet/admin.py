from django.contrib import admin
from charactersheet.models.character_general_info import GeneralCharacterInfo
from charactersheet.models.character_base_statistics import CharacterBaseStatistics

# Register your models here.

admin.site.register(GeneralCharacterInfo)
admin.site.register(CharacterBaseStatistics)
