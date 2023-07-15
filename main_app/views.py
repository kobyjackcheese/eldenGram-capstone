from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Build, Character, Spell, Weapon, Talisman, Helmet, Chestplate, Gloves, Leggings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.core.exceptions import ValidationError



class Home(TemplateView):
    template_name = "home.html"

class CharacterList(TemplateView):
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["characters"] = Character.objects.all()
        return context
    
class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'img', 'description']
    template_name = "character_update.html"
    success_url = "/characters/"
    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})
    
class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"

class CharacterCreate(CreateView):
    model = Character
    fields = ["name", "img", "description", "vigStat", "mindStat", "endStat", "strStat", "dexStat", "intStat", "faiStat", "arcStat"]
    template_name = "character_create.html"
    success_url = "/characters/"
    Character.objects.get()
    
class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spells"] = Spell.objects.all()
        context["weapons"] = Weapon.objects.all()
        context["talismans"] = Talisman.objects.all()
        context["helmets"] = Helmet.objects.all()
        context["chestplates"] = Chestplate.objects.all()
        context["gloves"] = Gloves.objects.all()
        context["leggings"] = Leggings.objects.all()
        return context
    
class BuildDetail(DetailView):
    model = Character
    template_name = "build_detail.html"

class CharacterSpellAssoc(View):

    def get(self, request, pk, spell_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).spells.remove(spell_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).spells.add(spell_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("Cannot assign more than 6 spells to a character.")
        return redirect('character_detail', pk=pk)
    

class CharacterWeaponAssoc(View):

    def get(self, request, pk, weapon_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).weapons.remove(weapon_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).weapons.add(weapon_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("")
        return redirect('character_detail', pk=pk)
    

class CharacterTalismanAssoc(View):

    def get(self, request, pk, talisman_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).talismans.remove(talisman_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).talismans.add(talisman_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("")
        return redirect('character_detail', pk=pk)
    

class CharacterHelmetAssoc(View):

    def get(self, request, pk, helmet_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).helmet.remove(helmet_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).helmet.add(helmet_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("")
        return redirect('character_detail', pk=pk)
    

class CharacterChestplateAssoc(View):

    def get(self, request, pk, chestplate_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).chestplate.remove(chestplate_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).chestplate.add(chestplate_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("")
        return redirect('character_detail', pk=pk)
    
class CharacterGlovesAssoc(View):

    def get(self, request, pk, gloves_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).gloves.remove(gloves_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).gloves.add(gloves_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("")
        return redirect('character_detail', pk=pk)
    
class CharacterLeggingsAssoc(View):

    def get(self, request, pk, leggings_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Character.objects.get(pk=pk).leggings.remove(leggings_pk)
        if assoc == "add":
            try:
                Character.objects.get(pk=pk).leggings.add(leggings_pk)
            except ValidationError as e: 
                print(e)
                # raise ValidationError("")
        return redirect('character_detail', pk=pk)

        
        

