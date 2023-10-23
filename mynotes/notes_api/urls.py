from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('note/<str:pk>/', views.getNote, name='note'),
    path('note/<str:pk>/update', views.updateNote, name='updatenotes'),


]