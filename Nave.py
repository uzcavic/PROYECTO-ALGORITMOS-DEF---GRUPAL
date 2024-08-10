class Vehiculo:
    def __init__(self, nombre, longitud, capacidad_carga, crew, pasajeros, pilotos):
        self.nombre = nombre
        self.longitud = longitud
        self.capacidad_carga = capacidad_carga
        self.crew = crew
        self.pasajeros = pasajeros
        self.pilotos = pilotos
        
    def showVehiculo(self):
        print(f"Nombre: {self.nombre}\nLongitud: {self.longitud}\nCapacidad de carga: {self.capacidad_carga}\nPasajeros: {self.pasajeros}\nPilotos: {self.pilotos}\n") 

class Nave(Vehiculo):
    def __init__(self, nombre, longitud, capacidad_carga, crew, pasajeros, pilotos, hiperdrive, MGLT):
        super().__init__(nombre, longitud, capacidad_carga, crew, pasajeros, pilotos)
        self.hiperdrive = hiperdrive
        self.MGLT = MGLT
        
    def showNave(self):
        self.showVehiculo()
        print(f"Hiperpropulsor: {self.hiperdrive}\nMGLT: {self.MGLT}\n")
