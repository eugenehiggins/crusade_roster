from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, help_text='short description i.e. "5 intercessors')
    power = models. PositiveSmallIntegerField(default=0)
    points = models. PositiveSmallIntegerField(default=0)
    crusade_points = models. PositiveSmallIntegerField(default=0)
    battles_fought = models. PositiveSmallIntegerField(default=0)
    battles_survived = models. PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name
