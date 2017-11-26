from django import forms
from sgc.models import Empleado


#Se crea el formulario con los campos que se quiera, ya que es diferente 
#al de los modelos y se puede añadir a una vista
class LogForm(forms.Form):
	usuario = forms.CharField(max_length=20)
	contraseña = forms.CharField(max_length=20)

class RegEmpleado(forms.Form):

	nombre = forms.CharField(max_length=20)
	apellido = forms.CharField(max_length=20)
	cedula = forms.IntegerField()
	celular = forms.IntegerField()
	municipio = forms.CharField(max_length=20)
	ocupacion = forms.CharField(max_length=20)
	#municipio = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=Empleado.MUNICIPIOS)
	#ocupacion = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=Empleado.OCUPACIONES)

class RegCotizacion(forms.Form):

	nombre_de_la_finca = forms.CharField(max_length=30)
	telefono = forms.IntegerField()
	municipio = forms.CharField(max_length=20)
	cantidad_de_dias_por_semana = forms.IntegerField()
	cantidad_de_horas_por_dia = forms.IntegerField()
