# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-01 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oidc_provider", "0019_auto_20161005_1552"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="_post_logout_redirect_uris",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Enter each URI on a new line.",
                verbose_name="Post Logout Redirect URIs",
            ),
        ),
    ]
