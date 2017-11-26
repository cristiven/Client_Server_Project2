from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import LogForm, RegEmpleado, RegCotizacion 
from .models import Recolector,Empleado,Cotizacion


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

def empleado(request):
	form = RegEmpleado()
	form = RegEmpleado(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		nom = form_data.get("nombre")
		ape = form_data.get("apellido")
		ced = form_data.get("cedula")
		cel = form_data.get("celular")
		mun = form_data.get("municipio")
		ocu = form_data.get("ocupacion")
		obj = Empleado.objects.create(nombre=nom, apellido=ape, cedula=ced, celular=cel, municipio=mun, ocupacion=ocu)
	
	context = {
		"reg_empleado": form,
	}
	return render(request, 'empleo.html', context)

def cotizacion(request):
	form = RegCotizacion()
	form = RegCotizacion(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		nom_fin = form_data.get("nombre_de_la_finca")
		tele_fin = form_data.get("telefono_de_la_finca")
		municipio = form_data.get("municipio")
		dias_sem = form_data.get("cantidad_de_dias_por_semana")
		cant_horas = form_data.get("cantidad_de_horas_por_dia")
		obj = Cotizacion.objects.create(nombre_de_la_finca=nom_fin, telefono=tele_fin, municipio=municipio, cantidad_de_dias_por_semana=dias_sem, cantidad_de_horas_por_dias=cant_horas)
	
	context = {
		"reg_cotizacion": form,
	}
	return render(request, 'cotizacion.html', context)
	

# vistas para el chat

