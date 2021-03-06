# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 19:13
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fobi', '0013_formwizardentry_show_all_navigation_buttons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='title',
            field=models.CharField(blank=True, help_text='Shown in templates if available.', max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='formwizardentry',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='formwizardentry',
            name='title',
            field=models.CharField(blank=True, help_text='Shown in templates if available.', max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='formwizardentry',
            name='wizard_type',
            field=models.CharField(choices=[('SessionWizardView', 'Session wizard'), ('CookieWizardView', 'Cookie wizard')], default='SessionWizardView', help_text='Type of the form wizard.', max_length=255, verbose_name='Type'),
        ),
    ]
