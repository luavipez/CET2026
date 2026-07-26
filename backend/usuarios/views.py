from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson.objectid import ObjectId
import json
from backend.db import usuarios_collection

@csrf_exempt
def usuarios_list(request):
    if request.method == 'GET':
        # Obtener todos los usuarios
        usuarios = list(usuarios_collection.find())
        for u in usuarios:
            u['_id'] = str(u['_id']) # Convertir ObjectId a String para JSON
        return JsonResponse(usuarios, safe=False)

    elif request.method == 'POST':
        # Crear un usuario
        data = json.loads(request.body)
        if not data.get('nombre') or not data.get('email'):
            return JsonResponse({'error': 'Datos incompletos'}, status=400)
        
        nuevo_usuario = {
            'nombre': data['nombre'],
            'email': data['email']
        }
        resultado = usuarios_collection.insert_one(nuevo_usuario)
        nuevo_usuario['_id'] = str(resultado.inserted_id)
        return JsonResponse(nuevo_usuario, status=201)

@csrf_exempt
def usuario_detail(request, id):
    if request.method == 'DELETE':
        # Eliminar un usuario
        resultado = usuarios_collection.delete_one({'_id': ObjectId(id)})
        if resultado.deleted_count == 1:
            return JsonResponse({'mensaje': 'Usuario eliminado'}, status=200)
        return JsonResponse({'error': 'No encontrado'}, status=404)
