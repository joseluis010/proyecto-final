from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

import folium

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages 
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import forms, models


# Create your views here.

def index(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")


# def login(request):
#     return render(request, "home/login.html")


# @staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"messages": "Usuario creado 👌"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})




def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {"messages": f"Se ha logueado correctamente."})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form} )



def buscar(request):
    if request.method == 'POST':
        form = forms.BuscarForm(request.POST)
        if form.is_valid():
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            
            calles = models.Calle.objects.filter(ciudad__nombre=ciudad, ciudad__pais__nombre=pais)
            if calles:
                initialMap = folium.Map(location = [-34.90590178924003, -56.185210539997854], zoom_start=9)
                return render(request, 'home/buscar.html', {'calles': calles, 'map': initialMap._repr_html_()})
            else:
                messages.info(request, 'No se encontraron calles en la ciudad buscada.')
        
    else:
        form = forms.BuscarForm()

    return render(request, 'home/buscar.html', {'form': form})



def agregar_informacion(request):
    if request.method == 'POST':
        form = forms.AgregarInformacionForm(request.POST)
        if form.is_valid():
            pais = form.cleaned_data['pais']
            ciudad = form.cleaned_data['ciudad']
            calle = form.cleaned_data['calle']

            pais_obj, created = models.Pais.objects.get_or_create(nombre=pais)
            ciudad_obj, created = models.Ciudad.objects.get_or_create(nombre=ciudad, pais=pais_obj)

            # Verificar si la calle ya existe en la ciudad
            calle_obj, created = models.Calle.objects.get_or_create(nombre=calle, ciudad=ciudad_obj, pais=pais_obj )
            if created:
                # La calle ya existe, mostrar un mensaje de error o realizar alguna acción adicional
                    messages.error(request, 'La calle ha sido creada con exito.')
                    return redirect('home:agregar')

                # messages.success(request, 'Información agregada exitosamente.')  # Mensaje de éxito
                # return redirect('home:agregar')
            else:
                messages.error(request, 'La calle ya existe.')  # Mensaje de error
    else:
        form = forms.AgregarInformacionForm()

    return render(request, 'home/agregar_informacion.html', {'form': form})

