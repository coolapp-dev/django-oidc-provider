# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-02 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oidc_provider", "0008_rsakey"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rsakey",
            options={"verbose_name": "RSA Key", "verbose_name_plural": "RSA Keys"},
        ),
        migrations.AlterField(
            model_name="rsakey",
            name="key",
            field=models.TextField(help_text="Paste your private RSA Key here."),
        ),
    ]
