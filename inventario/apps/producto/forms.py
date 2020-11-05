from django import forms
from .models import Producto,Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto','marca','descripcion','valor']
        labels = {
            'nombre_producto': 'Nombre del Porducto',
            'marca': 'Marca Registrada',
            'descripcion': 'Describa las caracteristicas del producto',
            'valor': 'Ingrese un valor',
        }
        widgets = {
            'nombre_producto': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese el nombre del Producto'
          }
        ),
            'marca': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese la Marca del Producto'
          }
        ),
            'descripcion': forms.TextInput(
                attrs = {
                    'placeholder':'Decriba el Producto'
          }
        ),
            'valor': forms.TextInput(
               attrs = {
                    'placeholder':'Ingrese un valor ($)'
          }
        )
    }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut','nombre_cliente','apellidos','correo','celular','direccion']
        labels = {
            'rut': 'Rut del Cliente',
            'nombre_cliente': 'Nombres Paterno/Materno',
            'apellidos': 'Apellidoss Paterno/Materno',
            'correo': 'Correo Valido',
            'celular': 'Celular o Telefono',
            'direccion': 'Dirección Completa',
        }
        widgets = {
            'rut': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese su Rut'
          }
        ),
            'nombre_cliente': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese sus nombres Paterno y Materno'
          }
        ),
            'apellidos': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese sus apellidos Paterno y Materno'
          }
        ),
            'correo': forms.TextInput(
               attrs = {
                    'placeholder':'Ingrese su correo'
          }
        ),
            'celular': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese su Celular'
          }
        ),
            'direccion': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese su Dirección'
          }
        )
    }
