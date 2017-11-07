from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
#from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import ClienteForm, MenuForm
from clientes.models import Cliente, Orden, Menu
from django.contrib.auth.decorators import login_required
@login_required

def cliente_nuevo(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            orden = Cliente.objects.create(nombre=formulario.cleaned_data['nombre'],
            fecha_orden = formulario.cleaned_data['fecha_orden'],edad = formulario.cleaned_data['edad'],
            direccion = formulario.cleaned_data['direccion'],nit = formulario.cleaned_data['nit'])
            for menu_id in request.POST.getlist('clientes'):
                orden = Orden(menu_id=menu_id, orden_id = orden.id)
                orden.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente Guardada Exitosamente')
    else:
        formulario = ClienteForm()
    return render(request, 'peliculas/pelicula_editar.html', {'formulario': formulario})
# Create your views here.
#creamos listar

def cliente_editar(request, pk):
    orden = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        formulario = ClienteForm(request.POST, instance=orden)
        if formulario.is_valid():
            orden = formulario.save(commit=False)
            orden.save()
            return redirect('cliente_detalle', pk=orden.pk)
    else:
        formulario = ClienteForm(instance=orden)
    return render(request, 'peliculas/pelicula_editar.html', {'formulario': formulario})

@login_required
def cliente_list(request):
    #posts = Cliente.objects.filter(fecha_orden__lte=timezone.now()).order_by('fecha_orden')
    ordens = Cliente.objects.filter()
    return render(request, 'peliculas/listar_cliente.html', {'ordens': ordens})

def cliente_detalle(request, pk):
    orden = get_object_or_404(Cliente, pk=pk)
    return render(request, 'peliculas/cliente_detalle.html', {'orden': orden})


def cliente_remove(request, pk):
    orden = get_object_or_404(Cliente, pk=pk)
    orden.delete()
    return redirect('cliente_list')

def menu_detalle(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'peliculas/menu_detalle.html', {'menu': menu})

def menu_remove(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('menu_list')

def menu_list(request):
    menus = Menu.objects.filter()
    return render(request, 'peliculas/menu_lista.html', {'menus':menus})

def menu_editar(request,pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu_detalle', pk=menu.pk)
    else:
            form = MenuForm(instance=menu)
            return render(request,'peliculas/menu_nuevo.html',{'form':form})

def menu_nuevo(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = formu.save(commit=False)
            menu.save()
            return redirect('menu_list')
    else:
            form = MenuForm()
            return render(request,'peliculas/menu_nuevo.html',{'form':form})
