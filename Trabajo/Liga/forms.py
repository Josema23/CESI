from django import forms
from Liga.models import Jornada, Equipo, Jugador, Partido
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AutenticacionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets={'password': forms.PasswordInput(),}

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']


class FormJornada(forms.ModelForm):
    class Meta:
        model = Jornada
        fields= "__all__"

class FormEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields= "__all__"

class FormPartido(forms.ModelForm):
    class Meta:
        model = Partido
        fields= ['jornada', 'fecha','equipoLocal', 'resultado', 'equipoVisitante', 'estado']


class FormJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields= "__all__"
