from django.db import models
from django.utils.translation import ugettext_lazy as _
from charactersheet.models.choices import (
    AlignmentChoices,
    RaceChoices,
    ClassChoices,
    GenderChoices,
    SizeChoices,
)


class GeneralCharacterInfo(models.Model):

    name = models.CharField(
        max_length=50,
        null=False,
        verbose_name=_('Name')
    )

    alignment = models.CharField(
        choices=AlignmentChoices.choices(),
        max_length=30,
        null=False,
        verbose_name=_('Alignment')
    )

    player = models.CharField(
        max_length=50,
        null=True,
        verbose_name=_('Player name')
    )

    classes = models.CharField(
        choices=ClassChoices.choices(),
        max_length=40,
        verbose_name=_('Classes'),
        null=True
    )

    level = models.PositiveSmallIntegerField(
        verbose_name=_('Character level')
    )

    eye_color = models.CharField(
        max_length=20,
        verbose_name=_('Eye color')
    )

    age = models.PositiveSmallIntegerField(
        default=10,
        verbose_name=_('Age')
    )

    hair_color = models.CharField(
        max_length=25,
        verbose_name=_('Hair color'),
        null=True
    )

    homeland = models.CharField(
        max_length=50,
        verbose_name=_('Homeland'),
        null=True
    )

    deity = models.CharField(
        max_length=40,
        verbose_name=_('Deity'),
        null=True
    )

    height = models.PositiveSmallIntegerField(
        verbose_name=_('Height in centimeters')
    )

    weight = models.PositiveSmallIntegerField(
        verbose_name=_('Weight in kilograms')
    )

    size = models.CharField(
        choices=SizeChoices.choices(),
        verbose_name=_('Size'),
        max_length=10,
        null=True
    )

    gender = models.CharField(
        choices=GenderChoices.choices(),
        max_length=20,
        verbose_name=_('Gender')
    )

    race = models.CharField(
        choices=RaceChoices.choices(),
        verbose_name=_('Race'),
        max_length=20
    )

    def __str__(self):
        return self.name
