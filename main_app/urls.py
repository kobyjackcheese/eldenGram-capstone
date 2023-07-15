from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/spells/<int:spell_pk>/', views.CharacterSpellAssoc.as_view(), name="character_spell_assoc"),
    path('characters/<int:pk>/weapons/<int:weapon_pk>/', views.CharacterWeaponAssoc.as_view(), name="character_weapon_assoc"),
    path('characters/<int:pk>/talismans/<int:talisman_pk>/', views.CharacterTalismanAssoc.as_view(), name="character_talisman_assoc"),
    path('characters/<int:pk>/helmets/<int:helmet_pk>/', views.CharacterHelmetAssoc.as_view(), name="character_helmet_assoc"),
    path('characters/<int:pk>/chestplates/<int:chestplate_pk>/', views.CharacterChestplateAssoc.as_view(), name="character_chestplate_assoc"),
    path('characters/<int:pk>/gloves/<int:gloves_pk>/', views.CharacterGlovesAssoc.as_view(), name="character_gloves_assoc"),
    path('characters/<int:pk>/leggings/<int:leggings_pk>/', views.CharacterLeggingsAssoc.as_view(), name="character_leggings_assoc"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete',views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),

]