from django import forms
from .models import Genero, Usuario,Tour

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__"

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"