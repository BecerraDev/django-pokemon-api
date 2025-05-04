import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import CustomPokemon
from requests.exceptions import RequestException


# Obtener tipos dinámicamente desde la API
def get_pokemon_types():
    try:
        response = requests.get('https://pokeapi.co/api/v2/type')
        data = response.json()
        exclude_types = ['unknown', 'shadow', 'stellar']
        return [tipo['name'] for tipo in data['results'] if tipo['name'] not in exclude_types]
    except requests.exceptions.RequestException:
        return []


# Retorna a Home
def home(request):
    return render(request, 'core/home.html')


# Desconecta usuario autenticado
def exit(request):
    logout(request)
    return redirect('home')


# Página de error 404
def error_404_view(request, exception):
    return render(request, 'core/404.html', status=404)


# Conexión a la API externa
@login_required
def pokemon(request):
    type_filter = request.GET.get('type')
    limit = int(request.GET.get('limit', 20))
    pokemons = []

# Filtro por Tipo
    try:
        if type_filter:
            url = f'https://pokeapi.co/api/v2/type/{type_filter}'
            response = requests.get(url)
            data = response.json()
            for item in data['pokemon'][:limit]:
                details = requests.get(item['pokemon']['url']).json()
                pokemons.append({
                    'name': details['name'].capitalize(),
                    'image': details['sprites']['front_default'],
                    'types': [t['type']['name'] for t in details['types']],
                    'height': details['height'],
                    'weight': details['weight']
                })
    # Limitador busqueda
        else:
            url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}'
            response = requests.get(url)
            data = response.json()
            for item in data['results']:
                details = requests.get(item['url']).json()
                pokemons.append({
                    'name': details['name'].capitalize(),
                    'image': details['sprites']['front_default'],
                    'types': [t['type']['name'] for t in details['types']],
                    'height': details['height'],
                    'weight': details['weight']
                })
    # Validacion si tiene internet 

    except RequestException:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'API no disponible'}, status=503)
        else:
            return render(request, 'core/pokemon.html', {
                'pokemons': [],
                'types': get_pokemon_types(),
                'type': type_filter,
                'limit': limit,
                'error': 'La API de Pokémon no está disponible por el momento.'
            })
    # Creación de Array
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('pokemon_api/pokemon_results.html', {'pokemons': pokemons})
        return JsonResponse({'html': html})

    return render(request, 'core/pokemon.html', {
        'pokemons': pokemons,
        'types': get_pokemon_types(),
        'type': type_filter,
        'limit': limit
    })


# CRUD - Agregar Pokémon personalizado
def add_pokemon(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        image = request.POST.get('image')

        new_pokemon = CustomPokemon(name=name, type=type, image=image)
        new_pokemon.save()
        messages.success(request, 'Pokémon agregado exitosamente.')

        return redirect('pokemon')

    return render(request, 'pokemon/add.html', {
        'types': get_pokemon_types()
    })


# CRUD - Listar Pokémon personalizados
@login_required
def pokemon_list(request):
    custom_pokemons = CustomPokemon.objects.all()
    return render(request, 'pokemon/list.html', {'custom_pokemons': custom_pokemons})


# CRUD - Borrar Pokémon personalizado
@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(CustomPokemon, pk=pokemon_id)
    pokemon.delete()
    messages.success(request, f'Pokémon "{pokemon.name}" eliminado exitosamente.')
    return redirect('pokemon')


# CRUD - Editar Pokémon personalizado
@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(CustomPokemon, pk=pokemon_id)

    if request.method == 'POST':
        pokemon.name = request.POST.get('name')
        pokemon.type = request.POST.get('type')
        pokemon.height = request.POST.get('height')
        pokemon.weight = request.POST.get('weight')
        pokemon.image = request.POST.get('image')
        pokemon.save()
        return redirect('pokemon_list')

    return render(request, 'core/pokemon/edit.html', {
        'pokemon': pokemon,
        'types': get_pokemon_types()
    })