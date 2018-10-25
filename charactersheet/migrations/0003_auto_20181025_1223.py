# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charactersheet', '0002_auto_20181025_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalcharacterinfo',
            name='age',
            field=models.PositiveSmallIntegerField(default=10, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='generalcharacterinfo',
            name='alignment',
            field=models.CharField(choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'), ('LN', 'Lawful Neutral'), ('TN', 'True Neutral'), ('CN', 'Chaotic Neutral'), ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')], max_length=30, verbose_name='Alignment'),
        ),
        migrations.AlterField(
            model_name='generalcharacterinfo',
            name='classes',
            field=models.CharField(choices=[('BARD', 'Bard'), ('BARBARIAN', 'Barbarian'), ('CLERIC', 'Cleric'), ('DRUID', 'Druid'), ('FIGHTER', 'Fighter'), ('MONK', 'Monk'), ('PALADIN', 'Paladin'), ('RANGER', 'Ranger'), ('ROGUE', 'Rogue'), ('SORCERER', 'Sorcerer'), ('WIZARD', 'Wizard')], max_length=40, null=True, verbose_name='Classes'),
        ),
        migrations.AlterField(
            model_name='generalcharacterinfo',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Femala')], max_length=20, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='generalcharacterinfo',
            name='race',
            field=models.CharField(choices=[('ELF', 'Elf'), ('DWARF', 'Dwarf'), ('GNOME', 'Gnome'), ('HUMAN', 'Human'), ('HALF_ELF', 'Half-elf'), ('HALF_ORC', 'Half-orc'), ('HALFLING', 'Halfling')], max_length=20, verbose_name='Race'),
        ),
        migrations.AlterField(
            model_name='generalcharacterinfo',
            name='size',
            field=models.CharField(choices=[('TINY', 'Tiny'), ('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('HUGE', 'Huge')], max_length=10, null=True, verbose_name='Size'),
        ),
    ]