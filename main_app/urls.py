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


]