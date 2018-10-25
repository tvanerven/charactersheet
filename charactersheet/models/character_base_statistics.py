from django.db import models
from django.utils.translation import ugettext_lazy as _


class CharacterBaseStatistics(models.Model):

    character = models.ForeignKey(
        'GeneralCharacterInfo',
        on_delete=models.CASCADE
    )

    strength = models.PositiveSmallIntegerField(
        verbose_name=_('Strength')
    )

    dexterity = models.PositiveSmallIntegerField(
        verbose_name=_('Dexterity')
    )

    constituation = models.PositiveSmallIntegerField(
        verbose_name=_('Constitution')
    )

    intelligence = models.PositiveSmallIntegerField(
        verbose_name=_('Intelligence')
    )

    wisdom = models.PositiveSmallIntegerField(
        verbose_name=_('Wisdom')
    )

    charisma = models.PositiveSmallIntegerField(
        verbose_name=_('Charisma')
    )

    def __str__(self):
        return self.character.name
