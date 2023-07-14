from django.shortcuts import render, redirect
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Build, Character, Spell, Weapon, Talisman
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.core.exceptions import ValidationError



class Home(TemplateView):
    template_name = "home.html"

class BuildList(TemplateView):
    template_name = "build_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["builds"] = Build.objects.all()
        return context
    
class BuildCreate(CreateView):
    model = Build
    fields = ['name', 'img', 'description']
    template_name = "build_create.html"
    def get_success_url(self):
        return reverse('build_detail', kwargs={'pk': self.object.pk})

class BuildDetail(DetailView):
    model = Build
    template_name = "build_detail.html"

class BuildUpdate(UpdateView):
    model = Build
    fields = ['name', 'img', 'description']
    template_name = "build_update.html"
    def get_success_url(self):
        return reverse('build_detail', kwargs={'pk': self.object.pk})
    
class BuildDelete(DeleteView):
    model = Build
    template_name = "build_delete_confirmation.html"
    success_url = "/builds/"

class CharacterList(TemplateView):
    template_name = "character_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["characters"] = Character.objects.all()
        return context
    
class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["spells"] = Spell.objects.all()
        context["weapons"] = Weapon.objects.all()
        context["talismans"] = Talisman.objects.all()
        return context

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


    
# @method_decorator(login_required, name='dispatch')
# class ArtistList(TemplateView):
#     template_name = "artist_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         name = self.request.GET.get("name")
#         if name != None:
#             context["artists"] = Artist.objects.filter(
#                 name__icontains=name, user=self.request.user)
#             context["header"] = f"Searching for {name}"
#         else:
#             context["artists"] = Artist.objects.filter(user=self.request.user)
#             context["header"] = "Trending Artists"
#         return context

        
        

