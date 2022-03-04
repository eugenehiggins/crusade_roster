from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from unit.models import Unit, Weapon, Agenda


class WeaponsInline(admin.TabularInline):
    model = Weapon
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'width': 5})},
        # models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


class AgendasInline(admin.TabularInline):
    model = Agenda.units.through
    extra = 0


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "_weapons")
    search_fields = ["unit__name"]
    inlines = [
        WeaponsInline,
        AgendasInline,
    ]

    def _weapons(self, obj):
        return obj.weapons.all().count()


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    inlines = [
        AgendasInline,
    ]
    exclude = ('units',)


