# Generated by Django 4.0.2 on 2022-02-25 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0003_battle_unit_battles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='battles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unit.battle'),
        ),
    ]
