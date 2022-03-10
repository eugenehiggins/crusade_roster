# Generated by Django 4.0.2 on 2022-03-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_of_battle', '0019_alter_weapon_options_remove_profile_order_of_battle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('points_per_tally', models.PositiveSmallIntegerField(default=1, verbose_name='points gained per tally')),
                ('is_xp', models.BooleanField(default=True, help_text='Select if this is for xp; leave blank if for custom points')),
            ],
        ),
    ]
