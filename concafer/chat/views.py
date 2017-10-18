# Create your views here.
import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
import haikunator
from .models import Room
from django.http import HttpResponse

def about(request):
    return render(request, "chat/about.html")

def chat(request):
    return render(request, "chat/chat.html")

def new_room(request): 
    """
    Cree aleatoriamente una nueva sala y redireccione a ella.
    """
    new_room = None
    
    while not new_room:
        with transaction.atomic():
            label = haikunator.haikunate()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)

    return redirect(chat_room, label=label)


def chat_room(request, label):
    """
    Vista de la habitación: muestra la habitación con los últimos mensajes.
    La plantilla para esta vista tiene el negocio de WebSocket para enviar y transmitir mensajes, 
    así que vea la plantilla donde ocurre la magia.
    """
    # Si la habitación con la etiqueta dada no existe, cree automáticamente
    # a la primera visita (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # Queremos mostrar los últimos 50 mensajes, ordenados el más reciente-último
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
        'created' : created,
    })

def admin_chat(request):
    """
    La sala que muestra los tickets que se han creado
    """
    superusr = request.user.is_superuser


    if (superusr):
        rooms = Room.objects.order_by('label')
        return render(request, "chat/adminroom.html", {
            'rooms' : rooms,            
        })
    else:
        return render(request, "chat/disable.html")
