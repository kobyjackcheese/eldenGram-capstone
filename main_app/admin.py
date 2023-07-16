from django.contrib import admin
from .models import SpellType, Spell, Character, WeaponType, Weapon, Talisman, Helmet, Chestplate, Gloves, Leggings

# Register your models here.
admin.site.register(Character)
admin.site.register(SpellType)
admin.site.register(Spell)
admin.site.register(WeaponType)
admin.site.register(Weapon)
admin.site.register(Talisman)
admin.site.register(Helmet)
admin.site.register(Chestplate)
admin.site.register(Gloves)
admin.site.register(Leggings)