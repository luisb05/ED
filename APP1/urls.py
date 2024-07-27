from django.contrib import admin
from django.urls import path
from . import views  # Asegúrate de que tienes las vistas importadas

urlpatterns = [
    path('', views.index_view, name='index'),
    path('index/', views.index_view, name='index'),
    path('busquedas/', views.busquedas_view, name='busquedas'),
    path('search/', views.search, name='search'),
    path('admin/', admin.site.urls),
]
