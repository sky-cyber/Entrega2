from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProductoForm,ClienteForm
from .models import Producto,Cliente
from django.views.generic import TemplateView,ListView
from django.contrib.auth import authenticate,login
#from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'

# class registroProducto(CreateView):
#     model = Producto
#     form_class = ProductoForm
#     template_name = 'producto/registro_producto.html'
#     succes_url = reverse_lazy('producto:listar_producto')

def registroProducto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            messages.success(request,"Producto registrado correctamente")
            return redirect('producto:listar_producto')
    else:
        producto_form = ProductoForm()
    return render(request,'producto/registro_producto.html',{'producto_form':producto_form})


class listarProducto(ListView):
    model = Producto
    template_name='producto/listar_producto.html'
    context_object_name = 'listaproducto'
    queryset = Producto.objects.all()

# class editarProducto(UpdateView):
#     model = Producto
#     template_name = 'producto/registro_producto.html'
#     form_class = ProductoForm
#     succes_url = reverse_lazy('producto:listar_producto')

# def listarProducto(request):
#     listaproducto = Producto.objects.all()
#     return render(request,'producto/listar_producto.html',{'listaproducto':listaproducto})

def login(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')
        user = authenticate(request, username = username, password = passowrd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request,'El nombre de usuario o contraseña son incorrectos')
            return render(request, 'accounts/login.html', context)
    context = {}
    return render(request, 'accounts/login.html', context)


def editarProducto(request,id):
    error = None
    producto_form = None
    try:
        producto = Producto.objects.get(id = id)
        if request.method == 'GET':
            producto_form = ProductoForm(instance = producto)
        else:
            producto_form = ProductoForm(request.POST, instance = producto)
            if producto_form.is_valid():
                producto_form.save()
                messages.success(request,"Producto editado correctamente")
            return  redirect('producto:listar_producto')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'producto/registro_producto.html',{'producto_form':producto_form,'error':error})

def eliminarProducto(request,id):
    producto = Producto.objects.get(id = id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request,"Producto Eliminado correctamente")
        return redirect('producto:listar_producto')
    return render(request,'producto/eliminar_producto.html',{'producto':producto})


def registroCliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            messages.success(request,"Cliente registrado correctamente")
            return  redirect('producto:listar_cliente')
    else:
        cliente_form = ClienteForm()
    return render(request,'producto/registro_cliente.html',{'cliente_form':cliente_form})


def listarClientes(request):
    listarclientes = Cliente.objects.all()
    return render(request,'producto/listar_cliente.html',{'listarclientes':listarclientes})


def editarCliente(request,id):
    error = None
    cliente_form = None
    try:
        cliente = Cliente.objects.get(id = id)
        if request.method == 'GET':
            cliente_form = ClienteForm(instance = cliente)
        else:
            cliente_form = ClienteForm(request.POST, instance = cliente)
            if cliente_form.is_valid():
                cliente_form.save()
                messages.success(request,"Cliente Editado correctamente")
            return  redirect('producto:listar_cliente')
    except ObjectDoesNotExist as e:
        error = e
    return render(request,'producto/registro_cliente.html',{'cliente_form':cliente_form,'error':error})

def eliminarCliente(request,id):
    cliente = Cliente.objects.get(id = id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request,"Cliente Eliminado correctamente")
        return redirect('producto:listar_cliente')
    return render(request,'producto/eliminar_cliente.html',{'cliente':cliente})
