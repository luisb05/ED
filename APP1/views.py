from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
import json
import os

def index_view(request):
    return render(request, 'algoritmos/index.html')

def busquedas_view(request):
    return render(request, 'algoritmos/busquedas.html')

def load_data():
    file_path = os.path.join('app1', 'static', 'json', 'datos.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Datos cargados: {data}")
        return data
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return []

# Funciones de búsqueda
def busqueda_lineal(data, objetivo):
    print(f"Buscando de forma lineal el objetivo: {objetivo}") 
    return [item for item in data if item['valor'] == objetivo]

def busqueda_binaria(data, objetivo):
    print(f"Buscando de forma binaria el objetivo: {objetivo}")
    data.sort(key=lambda x: x['valor'])
    low, high = 0, len(data) - 1
    result = []
    while low <= high:
        mid = (low + high) // 2
        if data[mid]['valor'] == objetivo:
            # Encontrar todos los elementos que coincidan con el objetivo
            # Busca hacia la izquierda
            left = mid
            while left >= 0 and data[left]['valor'] == objetivo:
                result.append(data[left])
                left -= 1
            # Busca hacia la derecha
            right = mid + 1
            while right < len(data) and data[right]['valor'] == objetivo:
                result.append(data[right])
                right += 1
            break
        elif data[mid]['valor'] < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    return result

def busqueda_por_hash(data, objetivo):
    print(f"Buscando en hash el objetivo: {objetivo}")
    hash_table = {}
    for item in data:
        if item['valor'] not in hash_table:
            hash_table[item['valor']] = []
        hash_table[item['valor']].append(item)
    
    return hash_table.get(objetivo, [])

# Vista de búsqueda
def search(request):
    data = load_data()
    search_type = request.GET.get('type')
    objetivo = request.GET.get('objetivo')

    print(f"Tipo de búsqueda: {search_type}")
    print(f"Criterio de búsqueda: {objetivo}")

    if not search_type or not objetivo:
        return JsonResponse({'error': 'Invalid request parameters'}, status=400)

    if search_type == 'linear':
        result = busqueda_lineal(data, objetivo)
    elif search_type == 'binary':
        result = busqueda_binaria(data, objetivo)
    elif search_type == 'hash':
        result = busqueda_por_hash(data, objetivo)
    else:
        result = []

    print(f"Resultados de búsqueda: {result}")
    return JsonResponse(result, safe=False)


