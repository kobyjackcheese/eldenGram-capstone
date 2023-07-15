from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError



# Create your models here.
class Build(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SpellType(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Spell(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    SpellType = models.ForeignKey(SpellType, on_delete=models.CASCADE, related_name="spells")

    def __str__(self):
        return self.name
    
class WeaponType(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Weapon(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    WeaponType = models.ForeignKey(WeaponType, on_delete=models.CASCADE, related_name="spells")

    def __str__(self):
        return self.name
    
class Talisman(models.Model):

    name = models.CharField(default="", max_length=100)
    img = models.CharField(default="", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Helmet(models.Model):

    name = models.CharField(default="", max_length=100)
    img = models.CharField(default="", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Chestplate(models.Model):

    name = models.CharField(default="", max_length=100)
    img = models.CharField(default="", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Gloves(models.Model):

    name = models.CharField(default="", max_length=100)
    img = models.CharField(default="", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Leggings(models.Model):

    name = models.CharField(default="", max_length=100)
    img = models.CharField(default="", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


    



    # build model i made to test many to many relations that i will use as the build maker for final product
class Character(models.Model):

    name = models.CharField(max_length=150)
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    vigStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    mindStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    endStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    strStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    dexStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    intStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    faiStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    arcStat = models.IntegerField(default=0, validators=[MaxValueValidator(99)])
    
    
    #many to many relationships
    spells = models.ManyToManyField(Spell)
    weapons = models.ManyToManyField(Weapon)
    talismans = models.ManyToManyField(Talisman)
    helmet = models.ManyToManyField(Helmet)
    chestplate = models.ManyToManyField(Chestplate)
    gloves = models.ManyToManyField(Gloves)
    leggings = models.ManyToManyField(Leggings)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # if self.spells.count() > 6:
        #     raise ValidationError("Cannot assign more than 6 spells to a character.")
        # if self.weapons.count() > 2:
        #     raise ValidationError("Cannot assign more than 2 weapons to a character.")
        # if self.talismans.count() > 4:
        #     raise ValidationError("Cannot assign more than 4 talismans to a character.")

        super().save(*args, **kwargs)


        

