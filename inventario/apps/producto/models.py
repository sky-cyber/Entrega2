from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_producto = models.CharField('Nombre del Producto', max_length = 200 , blank = False, null = False)
    marca = models.CharField('Marca del Producto', max_length = 220 , blank = False, null = False)
    descripcion = models.TextField('Descripcion', blank = False, null = False)
    valor = models.IntegerField('Valor', blank = False, null = False)
    fecha_creacion = models.DateField('fecha de creacion', auto_now = True, auto_now_add = False)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto']

    def __str__(self):
        return self.nombre_producto


class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    rut = models.CharField('Rut', max_length = 200 , blank = False, null = False)
    nombre_cliente = models.CharField('Nombres del cliente', max_length = 200 , blank = False, null = False)
    apellidos = models.CharField('Apellidos del Cliente', max_length = 220 , blank = False, null = False)
    correo = models.EmailField('Correo Electrónico',blank = False, null = False)
    celular = models.IntegerField('celular', blank = False, null = False)
    direccion = models.CharField('Direccion',max_length = 100, blank = False, null = False)
    fecha_creacion = models.DateField('Fecha de Registro', auto_now = True, auto_now_add = False)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre_cliente']

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre_cliente)
