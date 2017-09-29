from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LogForm 
from .models import Recolector


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

