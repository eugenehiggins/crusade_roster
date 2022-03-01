# Generated by Django 4.0.2 on 2022-03-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0004_alter_unit_battles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='battles',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unit',
            name='description',
            field=models.CharField(blank=True, help_text='short description i.e. "5 intercessors', max_length=100),
        ),
    ]
