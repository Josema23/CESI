from .models import Jugador, Equipo, Partido, Jornada
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .forms import AutenticacionForm, RegistroForm, FormJornada, FormEquipo, FormPartido, FormJugador


#Mostrar los equipos de la liga

def listarEquipos(request):
    equipos = Equipo.objects.all().order_by('creacion')  #Cogemos todos los equipos de la base de datos, y ordenamos alfabetica.
    contexto = {'equipos':equipos}
    return render(request,'listarEquipos.html',contexto)

#Muestra un unico equipo seleccionado

def listarPlantilla(request, equipo_id):

    equipo = Equipo.objects.get(pk=equipo_id)
    plantilla = Jugador.objects.filter(equipo=equipo_id).order_by('-posicion', 'dorsal')
    contexto = {'equipo':equipo, 'plantilla':plantilla}
    return render(request,'listarJugadores.html',contexto)

def mostrarEquipo(request,equipo_id):   #pasamos request y un identificador
    equipo = Equipo.objects.get(pk = equipo_id) #escogemos so un equipo de la base de datos
    jugadores=Jugador.objects.filter(equipo=equipo_id)
    contexto = {'equipo':equipo, 'jugadores':jugadores}
    return render(request,'mostrarEquipo.html',contexto)    #Redirige hacia el html con la informacion


def mostrarJugador(request,equipo_id, jugador_id):   #pasamos request y un identificador

    jugador = Jugador.objects.get(pk = jugador_id) #escogemos so un equipo de la base de datos
    equipo = Jugador.objects.filter(equipo=equipo_id)
    contexto = {'jugador':jugador, 'equipo':equipo}
    return render(request,'Jugador.html',contexto)    #Redirige hacia el html con la informacion

#Muestra los equipos de la liga ordenados por los puntos que tenga

def clasificacion(request):
    clasificados = Equipo.objects.all().order_by('-puntos')  #ordenamos los equipos por puntos
    contexto={'clasificados':clasificados}
    return render(request,'clasificacion.html',contexto)

def calendario(request):

    jornadas =Jornada.objects.order_by('numJornada')
    contexto={'jornadas':jornadas}      #Nombre entre comillas es el objeto que se devuelve
    return render(request, 'calendario.html', contexto)

def mostrarJornada(request, jornada_id):

    print(jornada_id)
    jornada = Jornada.objects.get(pk = jornada_id) #pk = primary key
    partido = Partido.objects.filter(jornada = jornada_id).order_by('fecha')
    contexto = {'jornadas':jornada, 'partidos':partido}
    return render(request,'jornada.html',contexto)


def menuPrincipal(request):
    return render(request, 'menuPrincipal.html')

@login_required
def crearEquipo(request):
	equipo=Equipo()
	if request.method=="POST":
		formulario=FormEquipo(request.POST,request.FILES,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return redirect('/equipos/')
	else:
		formulario=FormEquipo()
	context={'formulario':formulario}
	return render(request,"crearEquipo.html",context)

@login_required
def modEquipo(request, equipo_id):
	equipo=Equipo.objects.get(pk=equipo_id)
	if request.method=="POST":
		formulario=FormEquipo(request.POST,request.FILES,instance=equipo)
		if formulario.is_valid():
			formulario.save()
			return redirect('/equipos/')
	else:
		formulario=FormEquipo(instance=equipo)
	context={'formulario':formulario, 'equipo':equipo}
	return render(request,"modificarEquipo.html",context)

@login_required
def borrarEquipo(request,equipo_id):
    equipo = get_object_or_404(Equipo, pk = equipo_id)
    equipo.delete()
    return redirect('/equipos/')


def usuarioLogin(request):
    if request.method=='POST':
        formulario = AutenticacionForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    return render(request, 'errorLogin.html')
            else:
                return render(request, 'errorLogin.html')
    else:
        formulario = AutenticacionForm()
    contexto = {'formulario':formulario,
                'navbar': "login"}
    return render(request,'login.html',contexto)

# Funcion para cerrar sesion en la pagina
@login_required(login_url='/login')
def usuarioLogout(request):
    logout(request)
    return redirect('/')

# Funcion para registrarse en la pagina
def usuarioRegistro(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = RegistroForm()
    contexto = {'formulario':formulario,
                'navbar': "registro"}
    return render(request,'registro.html',contexto)


@login_required
def crearJornada(request):
	jornada=Jornada()
	if request.method=="POST":
		formulario=FormJornada(request.POST,request.FILES,instance=jornada)
		if formulario.is_valid():
			formulario.save()
			return redirect('/calendario/')
	else:
		formulario=FormJornada()
	context={'formulario':formulario}
	return render(request,"crearJornada.html",context)


@login_required
def modNumJornada(request, jornada_id):
	jornada=get_object_or_404(Jornada, pk=jornada_id)
	if request.method=="POST":
		formulario=FormJornada(request.POST,request.FILES,instance=jornada)
		if formulario.is_valid():
			formulario.save()
			return redirect('/calendario/')
	else:
		formulario=FormJornada(instance=jornada)
	context={'formulario':formulario, 'jornada':jornada}
	return render(request,"modificarNumJornada.html",context)

@login_required
def borrarJornada(request,jornada_id):
    jornada = Jornada.objects.get(pk = jornada_id)
    jornada.delete()
    return redirect('/calendario/')


@login_required
def crearPartido(request, jornada_id):
    partido=Partido()
    jornada=Jornada.objects.get(pk=jornada_id)
    if request.method=="POST":
        formulario=FormPartido(request.POST,request.FILES,instance=partido)
        context={'formulario':formulario, 'jornada':jornada}
        if formulario.is_valid():
            formulario.save()
            return redirect('/calendario/')
        else:
            return render(request,"crearJugador.html",context)
    else:
        formulario=FormPartido()
        context={'formulario':formulario, 'jornada':jornada}
        return render(request,"crearPartido.html",context)

@login_required
def crearJugador(request, equipo_id):
    jugador=Jugador()
    equipo=Equipo.objects.get(pk=equipo_id)

    if request.method=="POST":
        formulario=FormJugador(request.POST,request.FILES,instance=jugador)
        context = {'formulario':formulario, 'equipo':equipo}

        if formulario.is_valid():
            formulario.save()
            return redirect('/equipos/')
        else:
            return render(request,"crearJugador.html",context)

    else:
        formulario=FormJugador()
        context = {'formulario':formulario, 'equipo':equipo}
        return render(request,"crearJugador.html",context)


@login_required
def modificarJugador(request, jugador_id, equipo_id):

    jugador=get_object_or_404(Jugador, pk=jugador_id)
    equipo=get_object_or_404(Equipo, pk=equipo_id)

    if request.method=="POST":
        formulario=FormJugador(request.POST,request.FILES,instance=jugador)

        if formulario.is_valid():
            formulario.save()
            return redirect('/equipos/')

    else:
        formulario=FormJugador(instance=jugador)
        context={'formulario':formulario,'jugador':jugador, 'equipo':equipo}
        return render(request,"modificarJugador.html",context)


@login_required
def borrarJugador(request,jugador_id, equipo_id):
    jugador = get_object_or_404(Jugador, pk = jugador_id)
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    jugador.delete()
    return redirect('/equipos/')



@login_required
def modificarPartido(request, jornada_id):

    partido=get_object_or_404(Jornada, pk=jornada_id)

    if request.method=="POST":
        formulario=FormPartido(request.POST,request.FILES,instance=partido)

        if formulario.is_valid():
            formulario.save()
            return redirect('/calendario/')

    else:
        formulario=FormPartido(instance=partido)
        context={'formulario':formulario,'partido':partido}
        return render(request,"modificarJugador.html",context)
