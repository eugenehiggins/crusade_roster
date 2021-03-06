from django.contrib import admin
from django.forms import TextInput, NumberInput
from django.db import models
from order_of_battle.models import Unit, Weapon, Profile, Agenda, Army


class WeaponsInline(admin.TabularInline):
    model = Weapon
    extra = 0
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'width': 5})},
        # models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }


class UnitsInline(admin.TabularInline):
    model = Unit
    fields = ('name', 'power', 'crusade_points')
    extra = 0


class ProfilesInline(admin.TabularInline):
    model = Profile
    extra = 1
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'class': 'profile-text-input'})},
        models.IntegerField: {'widget': NumberInput(attrs={'class': 'profile-number-input'})},
    }

    class Media:
        css = {
            'all': ('admin/css/my-admin.css',),
        }


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ["unit__name"]
    inlines = [
        ProfilesInline,
        WeaponsInline,
    ]

    def _weapons(self, obj):
        return obj.weapons.all().count()


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ("name", "is_xp")


@admin.register(Army)
class ArmyAdmin(admin.ModelAdmin):
    list_display = ("name", "general", "id")
    inlines = [
        UnitsInline,
    ]


