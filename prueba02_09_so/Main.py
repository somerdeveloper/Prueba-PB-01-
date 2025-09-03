from computadora import Computadora
from telefono import Telefono
from tablet import Tablet
from tienda import Tienda

#### TIENDA 
tienda = Tienda()

    # Crear dispositivos
compu = Computadora("Dell", "XPS 13", 1200000, 16)
celular = Telefono("Samsung", "Galaxy S22", 800000, 108)
tablet = Tablet("Apple", "iPad Air", 700000, 10.9)

    # Modificar el precio de la tablet
tablet.set_precio(750000)

    # Agregar dispositivos a la tienda
tienda.agregar_dispositivo(compu)
tienda.agregar_dispositivo(celular)
tienda.agregar_dispositivo(tablet)

    # Mostrar catálogo
tienda.mostrar_catalogo()



