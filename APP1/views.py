from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from collections import deque
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Lista
import json
import os

def index_view(request):
    return render(request, 'algoritmos/index.html')

def ver_lista(request):
    lista2 = Lista.objects.all()
    context = {'lista3': lista2}
    return render(request, 'algoritmos/basica.html', context)

def colas_view(request):
    return render(request, 'algoritmos/colas.html')

def pilas_view(request):
    return render(request, 'algoritmos/pilas.html')

def busquedas_view(request):
    return render(request, 'algoritmos/busquedas.html')

def ordenamiento_view(request):
    return render(request, 'algoritmos/ordenamientos.html')

#Esctructura de Datos lineales

# Función para cargar datos de cola------------------------------------------------------------------
# Ruta del archivo JSON
FILE_PATH = os.path.join('APP1', 'static', 'json', 'datacola.json')

# Función para cargar datos de cola
def load_dataCola():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return deque(data.get('cola', []))  # Convertir a deque para manejar la cola
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return deque()

# Función para guardar datos de cola
def save_dataCola(queue):
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump({'cola': list(queue)}, file, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Funciones de Colas
def enqueue(queue, item):
    queue.append(item)

def dequeue(queue):
    if not is_empty(queue):
        return queue.popleft()
    raise IndexError("Dequeue from empty queue")

def peek(queue):
    if not is_empty(queue):
        return queue[0]
    raise IndexError("Peek from empty queue")

def is_empty(queue):
    return len(queue) == 0

def size(queue):
    return len(queue)

# Vista de Colas (CRUD)
@csrf_exempt
@require_http_methods(["GET", "POST", "DELETE"])
def queue_view(request):
    queue = load_dataCola()  # Cargar la cola

    if request.method == "GET":
        operation = request.GET.get('operation')
        try:
            if operation == 'peek':
                item = peek(queue)
                return JsonResponse({'success': True, 'item': item})
            elif operation == 'size':
                return JsonResponse({'success': True, 'size': size(queue)})
            elif operation == 'is_empty':
                return JsonResponse({'success': True, 'is_empty': is_empty(queue)})
            else:
                return JsonResponse({'error': 'Operation not recognized'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            item = body.get('item')
            if item:
                enqueue(queue, item)
                save_dataCola(queue)
                return JsonResponse({'success': True, 'queue': list(queue)})
            else:
                return JsonResponse({'error': 'No item provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == "DELETE":
        try:
            item = dequeue(queue)
            save_dataCola(queue)
            return JsonResponse({'success': True, 'item': item, 'queue': list(queue)})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

# Función para cargar datos de pilas-------------------------------------------------------------------------
FILE_PATH = os.path.join('app1', 'static', 'json', 'datapila.json')

# Función para cargar datos de pila
def load_dataStack():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return deque(data.get('pila', []))  # Convertir a deque para manejar la pila
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return deque()

# Función para guardar datos de pila
def save_dataStack(stack):
    try:
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump({'pila': list(stack)}, file, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Funciones de Pila
def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    raise IndexError("Pop from empty stack")

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    raise IndexError("Peek from empty stack")

def is_empty(stack):
    return len(stack) == 0

def size(stack):
    return len(stack)

# Vista de Pila (CRUD)
@csrf_exempt
@require_http_methods(["GET", "POST", "DELETE"])
def stack_view(request):
    stack = load_dataStack()  # Cargar la pila

    if request.method == "GET":
        operation = request.GET.get('operation')
        try:
            if operation == 'peek':
                item = peek(stack)
                return JsonResponse({'success': True, 'item': item})
            elif operation == 'size':
                return JsonResponse({'success': True, 'size': size(stack)})
            elif operation == 'is_empty':
                return JsonResponse({'success': True, 'is_empty': is_empty(stack)})
            else:
                return JsonResponse({'error': 'Operation not recognized'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            item = body.get('item')
            if item:
                push(stack, item)
                save_dataStack(stack)
                return JsonResponse({'success': True, 'stack': list(stack)})
            else:
                return JsonResponse({'error': 'No item provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    elif request.method == "DELETE":
        try:
            item = pop(stack)
            save_dataStack(stack)
            return JsonResponse({'success': True, 'item': item, 'stack': list(stack)})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
#Algoritmo de Busqueda------------------------------------------------------------------------------------
def load_data():
    file_path = os.path.join('app1', 'static', 'json', 'datosbusquedas.json')
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

#Algoritmo de Ordenamiento-----------------------------------------------------------------------------------

def load_dataOrdenamiento(algorithm):
    file_path = os.path.join('app1', 'static', 'json', 'datosordenamiento.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get(algorithm, [])
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return []

# Funciones de Ordenamiento
def bubble_sort(data):
    data = list(data)
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j]['valor'] > data[j+1]['valor']:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def selection_sort(data):
    data = list(data)
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j]['valor'] < data[min_idx]['valor']:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def insertion_sort(data):
    data = list(data)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key['valor'] < data[j]['valor']:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]['valor']
    left = [x for x in data if x['valor'] < pivot]
    middle = [x for x in data if x['valor'] == pivot]
    right = [x for x in data if x['valor'] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(data):
    if len(data) <= 1:
        return data
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i]['valor'] < right[j]['valor']:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

# Vista de Ordenamiento
def sorting_view(request):
    algorithm = request.GET.get('algorithm')
    data = load_dataOrdenamiento(algorithm)

    if not data:
        return JsonResponse({'error': 'Datos no encontrados'}, status=404)

    try:
        if algorithm == 'bubble':
            sorted_data = bubble_sort(data)
        elif algorithm == 'selection':
            sorted_data = selection_sort(data)
        elif algorithm == 'insertion':
            sorted_data = insertion_sort(data)
        elif algorithm == 'quick':
            sorted_data = quick_sort(data)
        elif algorithm == 'merge':
            sorted_data = merge_sort(data)
        else:
            return JsonResponse({'error': 'Algoritmo no reconocido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(sorted_data, safe=False)


