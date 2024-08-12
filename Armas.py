
class Armas:
    def __init__(self, modelo, tipo, descripcion):
        self.modelo = modelo
        self.tipo = tipo
        self.descripcion = descripcion

    def showArmas(self):
        print(f"Modelo: {self.modelo}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}")
        