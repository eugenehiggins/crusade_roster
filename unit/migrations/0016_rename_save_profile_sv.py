# Generated by Django 4.0.2 on 2022-03-04 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0015_alter_profile_attacks_alter_profile_ballistic_skill_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='save',
            new_name='sv',
        ),
    ]
