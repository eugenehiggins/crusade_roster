# Generated by Django 4.0.2 on 2022-03-01 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_of_battle', '0006_weapon_delete_battle_remove_unit_battles_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weapon',
            options={'ordering': ('order_of_battle', 'name'), 'verbose_name': 'Weapon', 'verbose_name_plural': 'Weapons'},
        ),
        migrations.AlterField(
            model_name='weapon',
            name='order_of_battle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapons', to='order_of_battle.unit', verbose_name='order_of_battle'),
        ),
    ]