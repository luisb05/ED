from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('index/', views.index_view, name='index'),
    path('pilas/', views.pilas_view, name='pilas'),
    path('busquedas/', views.busquedas_view, name='busquedas'),
    path('ordenamientos/', views.ordenamiento_view, name='ordenamientos'),
    path('pila/', views.pila_view, name='pila_view'), 
    path('search/', views.search, name='search'), 
    path('sorting/', views.sorting_view, name='sorting_view'),
    path('admin/', admin.site.urls),
]
