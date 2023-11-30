from django.shortcuts import render
from django.http import HttpResponse
from AppBlog.forms import UserForm, KnitsForm, YarnsForm, AccesoriesForm
from AppBlog.models import Knits


# Create your views here.

def saludo(request):
    return HttpResponse("Welcome")
def crear_user_form(request):
    usuario_formulario = UserForm()
    contexto = {
        "form": usuario_formulario
    }
    return render (request, "AppBlog/crear_usuario.html", contexto)

def crear_knits_form(request):
    tejido_formulario = KnitsForm()
    contexto ={
        "form": tejido_formulario
    }
    return render(request, "AppBlog/agregar_tejido.html", contexto)

def crear_yarns_form(request):
    hilado_formulario = YarnsForm()
    contexto = {
        "form": hilado_formulario
    }
    return render(request,"AppBlog/agregar_hilado.html", contexto )

def crear_accesories_form(request):
    accesorios_formulario = AccesoriesForm()
    contexto = {
        "form": accesorios_formulario
    }
    return render(request,"AppBlog/agregar_accesorio.html", contexto)
def show_knits(request):
    tejidos = Knits.objects.all()
    contexto = {
        "Tejidos": tejidos
    }
    return render (request, "AppBlog/buscar_tejidos.html", contexto)
def search_knit(request):
    name = request.GET["name"]
    knits = Knits.objects.filter(name__icontains= name)
    contexto ={
        "Tejidos": knits
    }
    return render (request, "AppBlog/buscar_tejidos.html", contexto)