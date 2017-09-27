from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LogForm 
from .models import Recolector
from .models import Room

#@login_required
def home(request):
    return render(request, 'core/home.html')

def inicio(request):
	return render(request, 'inicio.html')


def LogOut(request):
	logout(request)
	return render(request, 'core/home.html')

def gd(request):
	return render(request, 'core/drive.html')

def login(request):
	form = LogForm()
	#Request.POST es para que el dato que se pida sea obligatorio
	form = LogForm(request.POST or None)
	if form.is_valid():
 		form_data = form.cleaned_data
 		user = form_data.get("usuario")
 		pas = form_data.get("contrasena")
 		obj = AdminCooperativa.objects.create(usuario=user,contrasena=pas)

	context = {
		"login_super_user": form,
	}
	return render(request, 'login_b.html', context)
	

# vistas para el chat

def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })