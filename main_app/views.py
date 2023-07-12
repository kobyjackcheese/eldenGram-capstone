from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Build, Character
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


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
        context["characters"] = Character.objects.all() # Here we are using the model to query the database for us.
        return context
    

# class Weapon:
#     def __init__(self, name, img):
#         self.name = name
#         self.img = img

# class Spell:
#     def __init__(self, name, img):
#         self.name = name
#         self.img = img

# class Stats:
#     def __init__(self, vig, mind, end, str, dex, int, fai, arc):
#         self.vig = vig
#         self.mind = mind
#         self.end = end
#         self.str = str
#         self.dex = dex
#         self.int = int
#         self.fai = fai
#         self.arc = arc



        
        

