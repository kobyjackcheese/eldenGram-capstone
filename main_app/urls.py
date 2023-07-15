from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('builds/', views.BuildList.as_view(), name="build_list"),
    path('builds/new/', views.BuildCreate.as_view(), name="build_create"),
    path('builds/<int:pk>/', views.BuildDetail.as_view(), name="build_detail"),
    path('builds/<int:pk>/update',views.BuildUpdate.as_view(), name="build_update"),
    path('builds/<int:pk>/delete',views.BuildDelete.as_view(), name="build_delete"),
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/spells/<int:spell_pk>/', views.CharacterSpellAssoc.as_view(), name="character_spell_assoc"),
    path('characters/<int:pk>/weapons/<int:weapon_pk>/', views.CharacterWeaponAssoc.as_view(), name="character_weapon_assoc"),
    path('characters/<int:pk>/talismans/<int:talisman_pk>/', views.CharacterTalismanAssoc.as_view(), name="character_talisman_assoc"),
    path('characters/<int:pk>/update',views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete',views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),

]