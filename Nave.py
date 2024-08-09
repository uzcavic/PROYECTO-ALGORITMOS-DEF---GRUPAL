class Nave:
    def __init__(self, nombre, longitud, capacidad_carga, clasificacion_hiperimpulsor, mgl):
        self.nombre = nombre
        self.longitud = longitud
        self.capacidad_carga = capacidad_carga
        self.clasificacion_hiperimpulsor = clasificacion_hiperimpulsor
        self.mgl = mgl
        
    def showNave(self):
        print(f"Nombre: {self.nombre}\nLongitud: {self.longitud}\nCapacidad de carga: {self.capacidad_carga}\nClasificación de hiperimpulsor: {self.clasificacion_hiperimpulsor}\n'MGLT: {self.mgl}\n")    