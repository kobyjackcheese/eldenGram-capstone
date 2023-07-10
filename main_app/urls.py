from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('builds/', views.BuildList.as_view(), name="build_list"),
    path('builds/new/', views.BuildCreate.as_view(), name="build_create"),
    path('builds/<int:pk>/', views.BuildDetail.as_view(), name="build_detail"),
]