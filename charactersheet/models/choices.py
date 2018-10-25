from enum import Enum
from django.utils.translation import ugettext_lazy as _


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class AlignmentChoices(ChoiceEnum):

    LG = _('Lawful Good')
    NG = _('Neutral Good')
    CG = _('Chaotic Good')
    LN = _('Lawful Neutral')
    TN = _('True Neutral')
    CN = _('Chaotic Neutral')
    LE = _('Lawful Evil')
    NE = _('Neutral Evil')
    CE = _('Chaotic Evil')


class RaceChoices(ChoiceEnum):

    ELF = _('Elf')
    DWARF = _('Dwarf')
    GNOME = _('Gnome')
    HUMAN = _('Human')
    HALF_ELF = _('Half-elf')
    HALF_ORC = _('Half-orc')
    HALFLING = _('Halfling')


class ClassChoices(ChoiceEnum):
    BARD = _('Bard')
    BARBARIAN = _('Barbarian')
    CLERIC = _('Cleric')
    DRUID = _('Druid')
    FIGHTER = _('Fighter')
    MONK = _('Monk')
    PALADIN = _('Paladin')
    RANGER = _('Ranger')
    ROGUE = _('Rogue')
    SORCERER = _('Sorcerer')
    WIZARD = _('Wizard')


class GenderChoices(ChoiceEnum):
    MALE = _('Male')
    FEMALE = _('Femala')


class SizeChoices(ChoiceEnum):
    TINY = _('Tiny')
    SMALL = _('Small')
    MEDIUM = _('Medium')
    LARGE = _('Large')
    HUGE = _('Huge')
