from django import forms


#Se crea el formulario con los campos que se quiera, ya que es diferente 
#al de los modelos y se puede añadir a una vista
class LogForm(forms.Form):
	usuario = forms.CharField(max_length=20)
	contraseña = forms.CharField(max_length=20)

class RegEmpleado(forms.Form):
	nombre = forms.CharField(max_length=20)
	apellido = forms.CharField(max_length=20)
	celular = forms.IntegerField()
	cedula = forms.IntegerField()
	ciudad = forms.CharField(max_length=20)
	labor = forms.CharField(max_length=20)