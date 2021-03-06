from django.urls import path
from . import views

app_name = 'superheros'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('delete_hero/<hero_id>', views.delete, name='delete'),
    path('edit/', views.edit, name='edit')
   
    
]