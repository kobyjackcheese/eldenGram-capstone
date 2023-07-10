from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Build
from django.views.generic.edit import CreateView
from django.views.generic import DetailView


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
    success_url = "/builds/"

class BuildDetail(DetailView):
    model = Build
    template_name = "build_detail.html"
    

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



        
        

