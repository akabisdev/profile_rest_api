# Generated by Django 2.2 on 2022-02-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_api', '0002_userfeedmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfeedmodel',
            old_name='status',
            new_name='status_text',
        ),
        migrations.RenameField(
            model_name='userfeedmodel',
            old_name='user',
            new_name='user_profile',
        ),
    ]
