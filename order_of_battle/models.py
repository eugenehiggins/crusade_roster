from django.db import models


class Army(models.Model):
    owner = models.ForeignKey('auth.User', related_name='armies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    general = models.CharField(max_length=100, null=True, blank=True, help_text="your name")
    battles = models.PositiveSmallIntegerField(default=0, null=True, blank=True,)
    battles_won = models.PositiveSmallIntegerField(default=0)
    custom_points = models.PositiveSmallIntegerField(default=0)
    custom_points_name = models.CharField(max_length=100, blank=True, help_text='e.g. virulence points')
    supply_limit = models.PositiveSmallIntegerField(default=0)
    supply_used = models.PositiveSmallIntegerField(default=0)
    total_rp = models.PositiveSmallIntegerField(default=0, verbose_name='Total requisition')
    spent_rp = models.PositiveSmallIntegerField(default=0, verbose_name='Spent requisition')
    crusade_faction = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Armies"
    
    def __str__(self):
        return self.name

    
class Unit(models.Model):
    army = models.ForeignKey(
        Army,
        related_name="units",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, blank=True, help_text='short description i.e. "5 intercessors')
    power = models.PositiveSmallIntegerField(default=0)
    points = models.PositiveSmallIntegerField(default=0)
    crusade_points = models.PositiveSmallIntegerField(default=0)
    xp = models.PositiveSmallIntegerField(default=0)
    battles_fought = models.PositiveSmallIntegerField(default=0)
    battles_survived = models.PositiveSmallIntegerField(default=0)
    # battles = models.PositiveSmallIntegerField(default=0)
    marked_for_greatness = models.PositiveSmallIntegerField(
        help_text="Number of times marked for greatness", default=0
    )
    misc_xp_gain_loss = models.PositiveSmallIntegerField(default=0,
        help_text="Miscellaneous XP gain or losses"
    )
    battle_honours = models.CharField(max_length=300, blank=True, null=True)
    battle_scars = models.CharField(max_length=300, blank=True, null=True)
    equipment = models.CharField(max_length=300, blank=True, null=True)
    warlord_trait = models.CharField(max_length=300, blank=True, null=True)
    relic = models.CharField(max_length=300, blank=True, null=True)
    notes = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return '%d: %s' % (self.id, self.name)


class Weapon(models.Model):
    unit = models.ForeignKey(
        Unit,
        related_name="weapons",
        verbose_name="unit",
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=0)
    range = models.CharField(max_length=10, default=0)
    type = models.CharField(max_length=20, default=0)
    strength = models.CharField(max_length=5, verbose_name="S")
    armor_piercing = models.CharField(max_length=2, verbose_name="AP")
    damage = models.CharField(max_length=10, verbose_name="D")
    description = models.CharField(max_length=255, help_text="e.g. blast, poison weapon 4+")

    class Meta:
        verbose_name = "Weapon"
        verbose_name_plural = "Weapons"
        ordering = ("unit", "name")


    def __str__(self):
        return self.name


class Profile(models.Model):
    unit = models.ForeignKey(
        Unit,
        related_name="profiles",
        verbose_name="unit",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, default="", null=True, blank=True)
    movement = models.PositiveSmallIntegerField(default=0, verbose_name="M", null=True, blank=True)
    weapon_skill = models.PositiveSmallIntegerField(default=0, verbose_name="WS", null=True, blank=True)
    ballistic_skill = models.PositiveSmallIntegerField(default=0, verbose_name="BS", null=True, blank=True)
    strength = models.PositiveSmallIntegerField(default=0, verbose_name="S", null=True, blank=True)
    toughness = models.PositiveSmallIntegerField(default=0, verbose_name="T", null=True, blank=True)
    wounds = models.PositiveSmallIntegerField(default=0, verbose_name="W", null=True, blank=True)
    attacks = models.PositiveSmallIntegerField(default=0, verbose_name="A", null=True, blank=True)
    leadership = models.PositiveSmallIntegerField(default=0, verbose_name="Ld", null=True, blank=True)
    sv = models.PositiveSmallIntegerField(default=0, verbose_name="Sv", null=True, blank=True)

    def __str__(self):
        return self.name


class Agenda(models.Model):
    name = models.CharField(max_length=100, default="", null=True, blank=True)
    points_per_tally = models.PositiveSmallIntegerField(default=1, verbose_name='points gained per tally')
    is_xp = models.BooleanField(default=True, help_text="Select if this is for xp; leave blank if for custom points")

    def __str__(self):
        return self.name
