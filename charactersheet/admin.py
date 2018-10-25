from django.contrib import admin
from charactersheet.models.character_general_info import GeneralCharacterInfo
from charactersheet.models.character_base_statistics import CharacterBaseStatistics


class CharacterBaseStatisticsInline(admin.StackedInline):
    model = CharacterBaseStatistics
    max_num = 1


class GeneralCharacterInfoAdmin(admin.ModelAdmin):
    inlines = [
        CharacterBaseStatisticsInline,
    ]


admin.site.register(GeneralCharacterInfo, GeneralCharacterInfoAdmin)
admin.site.register(CharacterBaseStatistics)
