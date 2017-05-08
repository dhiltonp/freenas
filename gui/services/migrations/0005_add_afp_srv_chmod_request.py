# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-19 10:54
from __future__ import unicode_literals

from django.db import migrations, models
from freenasUI import choices


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_s3_help_changes'),
    ]

    operations = [
        migrations.AddField(
            model_name='afp',
            name='afp_srv_chmod_request',
            field=models.CharField(choices=choices.AFP_CHMOD_REQUEST_CHOICES, default='preserve', help_text="Advanced permission control that deals with ACLs.\nignore - UNIX chmod() requests are completely ignored, use thisoption to allow the parent directory's ACL inheritance fullcontrol over new items.\npreserve - preserve ZFS ACEs for named users and groups orPOSIX ACL group mask\nsimple - just to a chmod() as requested without any extra steps", max_length=120, verbose_name='Chmod Request'),
        ),
    ]
