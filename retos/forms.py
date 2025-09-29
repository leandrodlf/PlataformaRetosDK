from django import forms
from .models import Reto

class RetoForm(forms.ModelForm):
    class Meta:
        model = Reto
        fields = ['titulo', 'descripcion', 'contenido', 'dificultad', 'tipo', 'categoria', 'respuesta_correcta', 'puntos']