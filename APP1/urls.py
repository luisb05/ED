# from django.urls import path
# from . import views

# urlpatterns = [
#     path('index/', views.index, name='index'),
# ]

from django.contrib import admin
from django.urls import path
from . import views  # Assuming you have views in the current directory

urlpatterns = [
    path('', views.index, name='index'),  # Add this line
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
]
