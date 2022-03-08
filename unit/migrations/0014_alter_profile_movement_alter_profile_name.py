# Generated by Django 4.0.2 on 2022-03-04 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0013_alter_profile_weapon_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='movement',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='M'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
