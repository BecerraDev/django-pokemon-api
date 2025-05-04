"""
URL configuration for login_python_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home, pokemon, exit, add_pokemon, pokemon_list , edit_pokemon , delete_pokemon

urlpatterns = [
    path('', home, name='home'),
    path('pokemon/', pokemon, name='pokemon'),  # Correcto
    path('logout/', exit, name='exit'),

    
        # Pokémon CRUD
    path('pokemon/add/', add_pokemon, name='add_pokemon'),
    path('pokemon/list/', pokemon_list, name='pokemon_list'),
    path('pokemon/edit/<int:pokemon_id>/', edit_pokemon, name='edit_pokemon'),
    path('pokemon/delete/<int:pokemon_id>/', delete_pokemon, name='delete_pokemon'),

]

