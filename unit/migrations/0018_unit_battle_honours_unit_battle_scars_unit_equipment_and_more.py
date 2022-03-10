# Generated by Django 4.0.2 on 2022-03-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0017_alter_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='battle_honours',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='battle_scars',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='equipment',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='relic',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='warlord_trait',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
