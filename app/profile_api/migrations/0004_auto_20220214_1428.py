# Generated by Django 2.2 on 2022-02-14 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0003_auto_20220214_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfeedmodel',
            old_name='status_text',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='userfeedmodel',
            old_name='user_profile',
            new_name='user',
        ),
    ]
