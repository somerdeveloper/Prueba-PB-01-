from computadora import Computadora
from telefono import Telefono
from tablet import Tablet

# Clase que representa la tienda
class Tienda:
    def _init_(self):
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)


    def mostrar_catalogo(self):
        print(f"\nCatálogo de {self.nombre}:")
        total = 0
        for d in self.dispositivos:
            print("-", d.descripcion())
            total += d.precio
        print(f"\nValor total de inventario: ${total}")
