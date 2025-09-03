class Dispositivo:
    def _init_(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio  # Encapsulado

    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio

    def descripcion(self):
        return f"Dispositivo marca {self.marca}, modelo {self.modelo}"