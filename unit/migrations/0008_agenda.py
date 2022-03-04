# Generated by Django 4.0.2 on 2022-03-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0007_alter_weapon_options_alter_weapon_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit', models.ManyToManyField(to='unit.Unit')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
