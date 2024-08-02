from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('index/', views.index_view, name='index'),
    path('busquedas/', views.busquedas_view, name='busquedas'),
    path('ordenamientos/', views.ordenamiento_view, name='ordenamientos'),
    path('search/', views.search, name='search'), 
    path('sorting/', views.sorting_view, name='sorting_view'),
    path('admin/', admin.site.urls),
]
