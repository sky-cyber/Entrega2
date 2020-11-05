from django.urls import path
from .views import registroProducto,listarProducto,editarProducto,eliminarProducto
from .views import registroCliente,listarClientes,editarCliente,eliminarCliente,Inicio
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('Inicio',Inicio.as_view(), name = 'index'),
    path('registro_producto/',(registroProducto), name = 'registro_producto'),
    path('listar_producto/',(listarProducto.as_view()), name = 'listar_producto'),
    path('editar_producto/<int:id>',(editarProducto), name = 'editar_producto'),
    path('eliminar_producto/<int:id>',(eliminarProducto), name = 'eliminar_producto'),
    path('registro_cliente/',(registroCliente), name = 'registro_cliente'),
    path('listar_cliente/',(listarClientes), name = 'listar_cliente'),
    path('editar_cliente/<int:id>',(editarCliente), name = 'editar_cliente'),
    path('eliminar_cliente/<int:id>',(eliminarCliente), name = 'eliminar_cliente')
]
