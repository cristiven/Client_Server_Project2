from django import forms


#Se crea el formulario con los campos que se quiera, ya que es diferente 
#al de los modelos y se puede añadir a una vista
class LogForm(forms.Form):
	nombre = forms.CharField(max_length=20)