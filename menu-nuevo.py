from Armas import Armas
def mostrar_menu_armas():
    print("Menú de selección de armas:")
    for i, arma in enumerate(arma):
        print(f"{i+1}. {arma.nombre}")
    print("8. Salir")
def seleccionar_armas(num_armas):
    armas_seleccionadas = []
    while True:
        mostrar_menu_armas()
        opcion = input("Ingresa el número del arma que deseas seleccionar (1-8) o 'salir' para terminar: ")
        if opcion == "8":
            print("Saliendo del menú de armas...")
            break
        if opcion.isdigit():
            indice = int(opcion) - 1
            if indice >= 0 and indice < len(Armas):
                if Armas[indice] not in armas_seleccionadas:
                    armas_seleccionadas.append(Armas[indice])
                    print(f"Has seleccionado el arma {Armas[indice].nombre}.")
                else:
                    print("Esta arma ya ha sido seleccionada. Elige otra.")
            else:
                print("Opción inválida. Intenta de nuevo.")
        else:
            print("Opción inválida. Intenta de nuevo.")
        if len(armas_seleccionadas) >= num_armas:
            print(f"Has seleccionado el número requerido de armas: {num_armas}.")
            break
    return armas_seleccionadas
########################################################################################################################
from Nave import Nave
from Personaje import Personaje
from Planeta import Planeta
def mostrar_menu_personajes(self):
    print("¡Hola viajero! aquí vas a poder escoger tus misiones")
    print("Menú de selección de personajes:")
    for i, personaje in enumerate(self.personaje_lista):
        print(f"{i + 1}. {personaje.nombre}")
    print(f"{len(self.personaje_lista) + 1}. Salir")

def seleccionar_personajes(self):
    personajes_seleccionados = []
    while True:
        self.mostrar_menu_personajes()
        opcion_pe = input("Ingresa el número del personaje que deseas seleccionar (7 max) o 'salir' para terminar: ")

        if opcion_pe == str(len(self.personajes) + 1): ##
            print("Saliendo del menú...")
            break
        if opcion_pe.isdigit():
            indice = int(opcion_pe) - 1
            if 0 <= indice < len(self.personajes): ##
                if self.personaje_lista[indice] not in personajes_seleccionados:
                    personajes_seleccionados.append(self.personajes[indice]) ##
                    print(f"Has seleccionado al personaje {self.personajes[indice].nombre}.") ##
                else:
                    print("Este personaje ya ha sido seleccionado. Elige otro.")
            else:
                print("Opción inválida. Intenta de nuevo.")
        else:
            print("Opción inválida. Intenta de nuevo.")
        if len(personajes_seleccionados) >= 7:
            print("Has alcanzado el límite de selección de personajes.")
            break

    if personajes_seleccionados:
        nombres_seleccionados = ", ".join([personaje.nombre for personaje in personajes_seleccionados])
        print(f"Perfecto, has elegido a {nombres_seleccionados}.")
    else:
        print("No has seleccionado ningún personaje.")

def mostrar_menu_planetas(self):
    print("Aquí podrás seleccionar el nombre del planeta para tu batalla:")
    for i, planeta in enumerate(self.planetas):
        print(f"{i + 1}.- {planeta.nombre}")
    print("99.- Salir")

def seleccionar_planeta(self):
    planeta_seleccionado = None
    while True:
        self.mostrar_menu_planetas()
        opcion_p = input("Ingresa aquí el número del planeta al que quieres viajar, o introduce 99 para salir: ")
        if opcion_p == "99":
            print("Saliendo del menú...")
            break
        if opcion_p.isdigit():
            indice = int(opcion_p) - 1
            if 0 <= indice < len(self.planeta_lista):
                planeta_seleccionado = self.planeta_lista[indice]
                print(f"Has seleccionado el planeta {planeta_seleccionado.nombre}")
            else:
                print("¡Opción inválida! Prueba con un número válido.")
        else:
            print("¡Opción inválida! Introduce un número válido.")

    if planeta_seleccionado:
        print(f"Perfecto, has elegido el planeta {planeta_seleccionado.nombre}.")
    else:
        print("No has seleccionado ningún planeta.")

def mostrar_menu_naves(self):
    print("Aquí podrás seleccionar el nombre de la nave en la que quieres viajar:")
    for i, nave in enumerate(self.naves): ##
        print(f"{i + 1}.- {nave.nombre}")
    print("99.- Salir")

def seleccionar_nave(self):
    nave_seleccionada = None
    while True:
        self.mostrar_menu_naves()
        opcion_n = input("Ingresa aquí el número de la nave al que quieres viajar, o introduce 99 para salir: ")
        if opcion_n == "99":
            print("Saliendo del menú...")
            break
        if opcion_n.isdigit():
            indice = int(opcion_n) - 1
            if 0 <= indice < len(self.naves):
                nave_seleccionada = self.naves[indice]
                print(f"Has seleccionado la nave {nave_seleccionada.nombre}")
            else:
                print("¡Opción inválida! Prueba con un número válido.")
        else:
            print("¡Opción inválida! Introduce un número válido.")

    if nave_seleccionada:
        print(f"Perfecto, has elegido la nave {nave_seleccionada.nombre}")
    else:
        print("No has seleccionado ninguna nave")

def crear_mision(self):  
    misiones_creadas = 0  #Nuevo-Contador para las misiones creadas

    while misiones_creadas <= 5:  # Permitir hasta 5 misiones
        print(f"\nMisión {misiones_creadas + 1}:")
        
        # Seleccionar un planeta
        print("Indiqueme el destino al que quiere ir")
        index = 1
        for planeta in self.planeta: ##
            planeta:Planeta
            print(f"{index}-{planeta.nombre}")
            index += 1
        elccion = int(input("--> "))
        planeta_1 = self.planeta[elccion - 1] ##

        # Seleccionar una nave
        print("Indiqueme la nave que quiere usar")
        index = 1
        for nave in self.nave:
            nave:Nave
            print(f"{index}-{nave.nombre}") ##
            index += 1
        elccion = int(input("--> "))
        nave_1 = self.nave[elccion - 1] ##

        # Seleccionar personajes
        personajes = []
        elige = True
        while len(personajes) < 7 and elige:
            print("Indiqueme el personaje que quiere usar ")
            index = 1
            for personaje in self.personaje: ##
                personaje: Personaje
                print(f"{index}.- {personaje.nombre}")
                index += 1
            elccion = int(input("--> "))
            personaje = self.personaje[elccion - 1] ##
            personajes.append(personaje)
            
            while True:
                otro = input("""¿Quieres elegir a otro personaje?
        1. Sí
        2. No 
---> """)
                if otro == "1":
                    break
                elif otro == "2":
                    elige = False
                    break
                else:
                    print("Opción inválida")
        armas = []
        while len(armas) != len(personajes):
            print("Indiqueme el arma que quiere usar ")
            index = 1
            for arma in self.arma: ##
                arma:Armas
                print(f"{index}-{arma.nombre}")
                index += 1
            elccion = int(input("--> "))
            arm = self.arma[elccion - 1] ## 
            armas.append(arm)
            print("Elige la misma cantidad de armas que de personajes escogidos\n")

        misiones_creadas += 1

        if misiones_creadas < 5:
            continuar = input("¿Deseas crear otra misión? (sí/no): ").strip().lower()
            if continuar != "sí":
                break
            #Siento que falta un else pero no sé

    print(f"Has creado un total de {misiones_creadas} misiones.")

    print(f"\nPerfecto viajero! Ahora podrás ver tus misiones creadas.")
    print(f"Tienes un total de {len(misiones_creadas)} misiones escogidas, detalladas a continuación:")
    
    for mision in misiones_creadas:
        print(f"\nNombre de la misión: {mision["nombre"]}")
        print(f"Planeta destino: {mision["planeta"]}")
        print(f"Combatientes: {", ".join(mision["combatientes"])}")
        print(f"Armas de los combatientes: {", ".join(mision["armas"])}")
        print(f"Nave de viaje: {mision["nave"]}")
    self.confirmar_modificaciones(misiones_creadas)  # Llamar a la función para confirmar modificaciones

def confirmar_modificaciones(self, misiones_creadas):
    while True:
        respuesta = input("""¿Estás conforme con las misiones escogidas?
                          1.- Sí
                          2.- No """).strip()
        if respuesta == "1":
            print("¡Genial! Tus misiones han sido guardadas.")
            break
        elif respuesta == "2":
            print("Vamos a modificar las misiones. Sé que quieres combatir con lo mejor")
            self.modificar_misiones(misiones_creadas)
            break
        else:
            print("Opción inválida. Por favor, ingresa 1 o 2.")

def modificar_misiones(self, misiones_creadas):
    while True:
        print("\nSelecciona la misión que deseas modificar:")
        i=1
        for mision in enumerate(misiones_creadas):
            # Aquí no sé si va un mision:Mision, no estoy claro
            print(f"{i + 1}. {mision['nombre']}")
            1+=1
        
        opcion = input("Ingresa el número de la misión que deseas modificar o 'salir' para terminar: ")
        
        if opcion.isdigit() and 1 <= int(opcion) <= len(misiones_creadas):
            mision_seleccionada = misiones_creadas[int(opcion) - 1]
            print(f"\nModificando la misión: {mision_seleccionada['nombre']}")
            
            print("Indique un nuevo planeta:")
            index = 1
            for planeta in self.planeta_lista:
                print(f"{index}-{planeta.nombre}")
                index += 1
            nueva_eleccion = int(input("--> "))
            mision_seleccionada['planeta'] = self.planeta[nueva_eleccion - 1].nombre

            print("Indique una nueva nave:")
            index = 1
            for nave in self.nave_lista:
                print(f"{index}-{nave.nombre}")
                index += 1
            nueva_eleccion = int(input("--> "))
            mision_seleccionada['nave'] = self.nave[nueva_eleccion - 1].nombre

            print("Indique los nuevos personajes:")
            personajes = []
            elige = True
            while len(personajes) < 7 and elige:
                print("Indiqueme el personaje que quiere usar ")
                index = 1
                for personaje in self.personaje:
                    print(f"{index}-{personaje.nombre}")
                    index += 1
                nueva_eleccion = int(input("--> "))
                personaje = self.personaje[nueva_eleccion - 1]
                personajes.append(personaje)
                mision_seleccionada['combatientes'] = [p.nombre for p in personajes]
                
                while True:
                    otro = input("""¿Quieres elegir a otro personaje?
        1. Sí
        2. No 
---> """)
                    if otro == "1":
                        break
                    elif otro == "2":
                        elige = False
                        break
                    else:
                        print("Opción inválida")

            print("Indique las nuevas armas:")
            armas = []
            while len(armas) != len(personajes):
                print("Indiqueme el arma que quiere usar ")
                index = 1
                for arma in self.arma:
                    print(f"{index}-{arma.nombre}")
                    index += 1
                nueva_eleccion = int(input("--> "))
                arm = self.arma[nueva_eleccion - 1]
                armas.append(arm)
                mision_seleccionada['armas'] = [a.nombre for a in armas]
                print("Elige la misma cantidad de armas que de personajes escogidos\n")

            print("Misión modificada exitosamente.")

        elif opcion.lower() == "salir":
            print("Saliendo del menú de modificaciones...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")