from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('builds/', views.BuildList.as_view(), name="build_list"),
]