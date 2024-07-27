from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
import os

def index_view(request):
    return render(request, 'algoritmos/index.html')

def busquedas_view(request):
    return render(request, 'algoritmos/busquedas.html')

# Cargar datos desde el archivo JSON
def load_data():
    file_path = os.path.join('static', 'json', 'datos.json')
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
    return [item for item in data if item['valor'] == objetivo]

def busqueda_binaria(data, objetivo):
    data.sort(key=lambda x: x['valor'])
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]['valor'] == objetivo:
            return [data[mid]]
        elif data[mid]['valor'] < objetivo:
            low = mid + 1
        else:
            high = mid - 1
    return []

def busqueda_por_hash(data, objetivo):
    hash_table = {item['valor']: item for item in data}
    return [hash_table[objetivo]] if objetivo in hash_table else []

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

