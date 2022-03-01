from django.db import models


# class Battle(models.Model):
#     name = models.CharField(max_length=200, null=True, help_text='Optional; e.g. "Battle of Vortrex Divide')
#     enemy = models.CharField(max_length=200, null=True)
class Weapon(models.Model):
    name = models.CharField(max_length=100,)


class Unit(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, blank=True, help_text='short description i.e. "5 intercessors')
    power = models. PositiveSmallIntegerField(default=0)
    points = models. PositiveSmallIntegerField(default=0)
    crusade_points = models. PositiveSmallIntegerField(default=0)
    battles_fought = models. PositiveSmallIntegerField(default=0)
    battles_survived = models. PositiveSmallIntegerField(default=0)
    # battles = models.PositiveSmallIntegerField(default=0)
    marked_for_greatness = models.PositiveSmallIntegerField(
        help_text="Number of times marked for greatness", default=0
    )
    misc_xp_gain_loss = models.PositiveSmallIntegerField(
        help_text="Miscellaneous XP gain or losses"
    )
    def __str__(self):
        return self.name


