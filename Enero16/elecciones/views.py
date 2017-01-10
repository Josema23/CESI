from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.base import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from elecciones.forms import *
from forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from elecciones.models import *
# Create your views here.


def menuPrincipal (request):

    circunscritos=Circunscripcion.objects.all()
    contexto={'circunscritos':circunscritos}
    return render(request, 'menuPrincipal.html', contexto)


def Login(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		user = request.POST['username']
		passw = request.POST['password']
		access = authenticate(username=user,password=passw)
		if access is not None:
			login(request,access)
			return HttpResponseRedirect('/')
	else:
		formulario = AuthenticationForm()
        contexto={'formulario':formulario}
        return render(request,"login.html",contexto)



class crearCircunscrito (View):
    form_class=circunscritoForm
    template_name="crearCircunscrito.html"

    @method_decorator(login_required)
    def get(self, request,*args,**kwargs):
        formulario=self.form_class()
        context={'formulario':formulario}
        return render(request, self.template_name, context)
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        formulario=self.form_class(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
        context={'formulario':formulario}
        return render(request,self.template_name,context)

class listarCircunscritos(View):
    template_name="listarCircunscritos.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            print "Admin"
        circunscritos=Circunscripcion.objects.all()
        contexto={'circunscritos':circunscritos}
        return render(request,self.template_name,contexto)

class detalleCirc(View):
    template_nombre="circunscripcionDetalle.html"
    def get(self,request,*args,**kwargs):
        id=self.kwargs['circunscrito_id']
        circunscrito=get_object_or_404(Circunscripcion,pk=id)
        contexto={'circunscrito':circunscrito}
        return render(request,self.template_nombre,contexto)
