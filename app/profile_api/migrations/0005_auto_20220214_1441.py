# Generated by Django 2.2 on 2022-02-14 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0004_auto_20220214_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfeedmodel',
            old_name='user',
            new_name='user_profile',
        ),
    ]
