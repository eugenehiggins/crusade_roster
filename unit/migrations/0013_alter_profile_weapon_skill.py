# Generated by Django 4.0.2 on 2022-03-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0012_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='weapon_skill',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='WS'),
        ),
    ]
