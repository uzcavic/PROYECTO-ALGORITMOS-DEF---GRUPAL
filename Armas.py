
class Armas:
    def __init__(self, uid, nombre,  modelo, tipo, descripcion):
        self.id = uid   
        self.nombre = nombre 
        self.modelo = modelo
        self.tipo = tipo
        self.descripcion = descripcion

    def showArmas(self):
        print(f"ID: {self.id}\nNombre: {self.nombre}\nModelo: {self.modelo}\nTipo: {self.tipo}\nDescripcion: {self.descripcion}\n")
        