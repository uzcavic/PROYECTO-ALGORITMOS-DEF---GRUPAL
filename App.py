
import requests
from Mision import Mision
from Usuario import Usuario
from Armas import Armas
from Pelicula import Pelicula
from Especie import Especie
from Personaje import Personaje
from Planeta import Planeta
from Nave import Nave, Vehiculo
import matplotlib.pyplot as plt #para instalar esta libreria se habre una nueva terminal, aparece en los tres puntos de arriba, ya abierto colocar "pip install matplotlib" y listo 
import pandas as pd
from statistics import mean, multimode

class APP:

    especie_lista = []
    pelicula_lista = []
    personaje_lista = []
    planeta_lista = []
    nave_lista = []
    vehiculos_lista = []
    csv_arma_lista = []
    usuario_lista = []
    mision_lista=[]
    personaje_especie = {}
    personaje_nave = {} 
    personaje_planeta = {} 
    CSV_planeta_lista = []
    CSV_nave_lista = [] 
    CSV_personaje_lista = []  
    
    
    def start(self):
            
            print('Cargando datos...')
            print('Espere un momento, esto podría tardar unos minutos...')
        
            self.CSV_Crear_planetas()
            self.CSV_crear_arma()
            self.CSV_Crear_nave()
            self.crear_pelicula() 
            self.crear_especies() 
            self.crear_planeta() 
            self.crear_personaje() 
            self.relacionar_personajes_con_planetas()
            self.crear_nave() 
            self.relacionar_vehiculos_y_naves_con_personajes()
            self.mostrar_menu()


        

    def mostrar_menu(self):
        while True:
            # Registro de usuario
            while True:
                print("Bienvenido a la galaxia de Star Wars! Necesitamos saber si eres un usuario registrado y si no regístese por favor.")
                uid = input("Ingrese su ID: ").strip()
                usuario_encontrado = next((u for u in self.usuario_lista if u.uid == uid), None)

                if usuario_encontrado:
                    print("Este ID ya está registrado.")
                    continuar = input("¿Desea continuar al menú? (si/no): ").strip().lower()
                    if continuar == 'si':
                        usuario = usuario_encontrado  # Asignar el usuario encontrado
                        break  
                    else:
                        print("Por favor, ingrese otro ID.")
                else:
                    nombre = input("Ingrese su nombre: ").strip()
                    nuevo_usuario = Usuario(uid, nombre, [])
                    self.usuario_lista.append(nuevo_usuario)  # Agregar el ID a la lista de usuarios
                    usuario = nuevo_usuario  # Asignar el nuevo usuario
                    print(f"Usuario {nombre} registrado con éxito.")
                    break  # Salir del bucle después de registrar

            # Mostrar el menú después de registrar
            while True:
                print("""Bienvenido viajero, indique qué desea saber del universo de Star Wars
                        1. Buscar personaje
                        2. Ver lista de especies
                        3. Ver lista de planetas
                        4. Gráficos de la población de los planetas
                        5. Gráficos diferenciadores de las naves
                        6. Estadísticas básicas sobre valores de la nave
                        7. Menú de misiones (aquí puedes crear, modificar y visualizar tus misiones)                  
                        8. Salir""")
                opcion = input("---> ").strip()

                if opcion == "1":
                    self.buscar_personaje()
                elif opcion == "2":
                    contador = 1
                    for especie in self.especie_lista:
                        especie: Especie
                        print(f"Especie N°{contador}\n")
                        especie.showEspecie()
                        contador += 1
                elif opcion == "3":
                    contador = 1
                    for planeta in self.planeta_lista:
                        planeta: Planeta
                        print(f"Planeta N°{contador}\n")
                        planeta.showPlaneta()
                        contador += 1
                elif opcion == "4":
                    self.grafica_planetas()
                elif opcion == "5":
                    self.Grafica_nave()
                elif opcion == "6":
                    self.Estadistica_nave()
                elif opcion == "7":
                    self.menu_misiones(usuario) 

                elif opcion == "8":    

                    print("""Gracias y que la fuerza te acompañe
                        
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣟⠛⠛⠛⠛⠛⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⢠⣿⣿⣿⣿⠿⣿⣿⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⡏⠉⠉⢉⣿⣿⣿⣿⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⡀⠀⠀⠀ ⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣾⣿⣿⣿⡟⠀⢻⣿⣿⣿⣧⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
    ⣤⣤⣤⣤⣤⣤⣤⣤⣤⣬⣿⣿⣿⣿⣿⣷⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⢀⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⡀⢸⣿⣿⣿⣿⡇⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠁⠀⠀⠀⠀⠿⠿⠿⠿⠇⠀⠀⠀⠸⠿⠿⠿⠟⠀⠀⠀⠀⠀⠻⠿⠿⠿⠇⠸⠿⠿⠿⠿⠇⠀⠀⠙⠛⠿⠿⠿⠿⠿⠿⠿⠿
    ⢻⣿⣿⣿⣿⡄⢠⣿⣿⣿⣿⣿⡆⠀⣾⣿⣿⣿⡟⠀⢀⣾⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣄⠀⠀⠀⠀⣠⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿
    ⠈⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣿⠁⠀⣼⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣇⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢠⣿⣿⣿⣿⠏⢿⣿⣿⣿⣇⠀⠀⠀⣿⣿⣿⣿⣿⣀⣀⣀⣼⣿⣿⣿⡟⠀⠀⢹⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀
    ⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⣿⣟⣀⣸⣿⣿⣿⣿⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠙⢿⣿⣿⣿⣿⣧⠀⠀⠀⠀
    ⠀⠀⠘⣿⣿⣿⣿⣿⣿⠋⣿⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⠇⠀⠀⠀
    ⠀⠀⠀⢻⣿⣿⣿⣿⡏⠀⢹⣿⣿⣿⣿⡟⠀⢀⣿⣿⣿⣿⡟⠛⠛⠛⠛⣿⣿⣿⣿⡆⠀⣿⣿⣿⣿⣿⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀
    ⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠉⠉⠉⠉⠁⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠉⠉⠉⠉⠉⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀                      """)
                    
                    break    
                elif opcion == "8":
                    print("Saliendo del menú...")
                    break  # Salir del menú principal
                else:
                    print("Opción inválida, intente de nuevo")

            if opcion == "8":
                continue  #volvemos al inicio   
        
    def menu_misiones(self, usuario):
        while True:
            print("""Menú de Misiones:
            1. Crear Misión
            2. Modificar Misión
            3. Visualizar Misiones
            4. Guardar Misiones      
            5. Volver al menú principal""")
            opcion_mision = input("---> ").strip()

            if opcion_mision == "1":
                self.crear_mision(usuario)  # Llama al método para crear una nueva misión
            elif opcion_mision == "2":
                self.modificar_misiones(usuario)  # Llama al método para modificar misiones existentes
            elif opcion_mision == "3":
                self.visualizar_misiones(usuario)  # Llama al método para visualizar las misiones
            elif opcion_mision == "4":
                self.guardar_misiones(usuario)    
            elif opcion_mision == "5":
                print("Volviendo al menú principal...")
                break  # Sale del bucle y vuelve al menú principal
            else:
                print("Opción inválida. Intenta de nuevo.")

    def buscar_personaje(self):
        busqueda = input("Ingrese parte del nombre del personaje a buscar: ").strip().lower()
        resultados = []

        for personaje in self.personaje_lista:
            personaje: Personaje
            # Comprobamos si la búsqueda está en el nombre del personaje
            if busqueda in personaje.nombre.lower():
                resultados.append(personaje)

        if not resultados:
            print("No se encontraron personajes que coincidan con la búsqueda.")
        else:
            print("Resultados de la búsqueda:")
            contador = 1  
            for personaje in resultados:
                print(f"Personaje N°{contador}\n")
                personaje.showPersonaje()  
                contador += 1  
                print("-" * 40) #esto es para que se vea mas ordenado

    def grafica_planetas(self):            
            nombre=[]
            poblacion=[]
            for planeta in self.CSV_planeta_lista:
                planeta:Planeta
                if planeta.habitantes == "unknown":
                    nombre.append(planeta.nombre)
                    poblacion.append(0)
                else:
                    nombre.append(planeta.nombre)
                    poblacion.append(float(planeta.habitantes))  
            plt.bar(nombre,poblacion, width=0.6)
            plt.title('Población de cada planeta')
            plt.xlabel('Nombre de planetas')
            plt.ylabel('Población')
            plt.xticks(rotation=90)
            plt.show()
                    
    def Grafica_nave(self):        
        carga =[]
        hiperpulsor=[]
        mglt=[]
        nombres=[]
        longtudes=[]
        for nave in self.CSV_nave_lista:
            datos =[]
            
            nave:Nave
            nombres.append(nave.nombre)
            if nave.longitud == "unknown":
                    longtudes.append(0)
                    datos.append(0)
            elif nave.longitud =="1,600":
                 longtudes.append(1600)        
            else:
                longtudes.append(float(nave.longitud))
                datos.append(nave.longitud)
            if nave.capacidad_carga == "unknown":
                    carga.append(0)
                    datos.append(0)
            else:
                carga.append(float(nave.capacidad_carga)) 
                datos.append(float(nave.capacidad_carga))    
            if nave.hiperdrive == "unknown":
                    hiperpulsor.append(0)
                    datos.append(0)
            else:
                datos.append(nave.hiperdrive)
                hiperpulsor.append(float(nave.hiperdrive))
            if nave.MGLT == "unknown":
                    mglt.append(0)
                    datos.append(0)
            else:
                mglt.append(float(nave.MGLT))
                datos.append(float(nave.MGLT))  
        while True: 
             Estadi_menu=input(f"""Indiqueme que graficas desea ver
{20*'-'}
    1. Gráficos de longitud
    2. Gráficos de capacidad de carga
    3. Gráficos de hiperpropulsor
    4. Gráficos de MGLT
    5. Volver
    ---> """)     
             if Estadi_menu=="1":          
                #plt.subplot(221)
                plt.title("Longitudes de las naves") 
                plt.bar(nombres,longtudes,label=("longitud"),color="blue",width=0.6)   
                plt.xlabel('Nombre de naves')
                plt.ylabel('Magnitud')
                plt.xticks(rotation=90)         
                plt.legend()
                plt.show()
                continue
             elif Estadi_menu=="2":
                #plt.subplot(222)
                plt.bar(nombres,carga,label=("carga"),color="red",width=0.6)   
                plt.title("Carga de naves")
                plt.xlabel('Nombre de naves')
                plt.ylabel('Magnitud')    
                plt.xticks(rotation=90)         
                plt.legend() 
                plt.show()
                continue 
             elif Estadi_menu=="3":
               #plt.subplot(223)
                plt.bar(nombres,hiperpulsor,label=("hiperpulso"),color="green",width=0.6)   
                plt.title("Hiperpulsor de naves") 
                plt.xlabel('Nombre de naves')
                plt.ylabel('Magnitud')   
                plt.xticks(rotation=90)         
                plt.legend()  
                plt.show()
                continue
             elif Estadi_menu=="4":
               #plt.subplot(224)
                plt.bar(nombres,mglt,label=("MGLB"),color="cyan",width=0.6)   
                plt.title("MGLT de naves")  
                plt.xlabel('Nombre de naves')
                plt.ylabel('Magnitud')  
                plt.xticks(rotation=90)         
                plt.legend() 
                plt.show()
                continue
             elif Estadi_menu=="5":
                  break
             else:
                  print("Valor inválido\n") 

    def Estadistica_nave(self): 
        vel_max =[]
        pro_vel=0
        hiperpulsor=[]
        pro_hipe=0
        mglt=[]
        pro_mglt=0
        costos=[]
        pro_costo=0
        a=0
        for nave in self.CSV_nave_lista:
            nave:Nave
            if nave.vel_max == "unknown" or nave.vel_max=="n/a":
                a+=1    
            elif nave.vel_max == "1000km":
                vel_max.append(1000)
            else:
                vel_max.append(float(nave.vel_max))
            if nave.costo == "unknown" or nave.costo=="n/a":
                a+=1
            else:
                costos.append(float(nave.costo))   
            if nave.hiperdrive == "unknown" or nave.hiperdrive=="n/a":
                a+=1
            else:
                hiperpulsor.append(float(nave.hiperdrive))
            if nave.MGLT == "unknown" or nave.MGLT=="n/a":
                a+=1
            else:
                mglt.append(float(nave.MGLT))
        for hiper in hiperpulsor:
            pro_hipe+=hiper
        pro_hipe/=len(hiperpulsor)  
        for mg in mglt:
            pro_mglt+=mg
        pro_mglt/=len(mglt)    
        for velocidades in vel_max:
            pro_vel+=velocidades
        pro_vel/=len(vel_max)    
        for cos in costos:
            pro_costo+=cos
        pro_costo/=len(costos)  
        moda_hipe = multimode(hiperpulsor)
        moda_mglt= multimode(mglt)
        moda_vlmx = multimode(vel_max)
        moda_costo= multimode(costos)
        hiperpulsor.sort()
        mglt.sort()
        vel_max.sort()
        costos.sort()
        max_hipe = hiperpulsor[len(hiperpulsor)-1]
        max_mglt= mglt[len(mglt)-1]
        max_vlmx = vel_max[len(vel_max)-1]
        max_costo = costos[len(costos)-1]
        min_hipe = hiperpulsor[0]
        min_mglt= mglt[0]
        min_vlmx = vel_max[0]
        min_costo = costos[0]
        while True: 
            Estadi_menu=input(f"""Indiqueme que estadistica quiere ver de las naves
{60*'-'}
    1. Estadística sobre los Hiperimpulsores
    2. Estadística sobre los MGLT
    3. Estadística sobre la velocidad máxima en atmósfera
    4. Estadística sobre el costo de las naves
    5. Volver
    ---> """)
            if Estadi_menu =="1":
                print(f"""
    hiperimpulsor promedio: {pro_hipe}
    moda de hiperimpulsores: {moda_hipe}
    máximo hiperimpulsor registrado: {max_hipe}
    mínimo hiperimpulsor registrado: {min_hipe}""")
                continue
            elif Estadi_menu =="2":
                print(f"""
    MGLT promedio: {pro_mglt}
    moda de MGLT: {moda_mglt}
    máximo MGLT registrado: {max_mglt}
    mínimo MGLT registrado: {min_mglt}""")
                continue
            elif Estadi_menu =="3":
                print(f"""
    Promedio de la velocidad máxima en atmósfera: {pro_vel}
    moda de la velocidad maxima en atmosfera: {moda_vlmx}
    máxima velocidad en atmosfera registrado: {max_vlmx}
    mínima velocidad en attmosfera registrado: {min_vlmx}""")
                continue
            elif Estadi_menu =="4":
                print(f"""
    Promedio de costo en credito de una nave: {pro_costo}
    moda de costo de nave: {moda_costo}
    máximo costo de una nave: {max_costo}
    mínimo costo de una nave: {min_costo}""")
                continue
                
            elif Estadi_menu=="5":
                break

    def crear_especies(self):

            for id_specie in range(1, 38): #hay 37 especies en total
                """print("Viendo especie: " + str(id_specie))"""
                id_specie = str(id_specie)
                url = f"https://www.swapi.tech/api/species/{id_specie}" #esto solo dará el nombre, id y la url de la especie
                response = requests.get(url)
                if response.status_code==200:
                    datos=response.json()
                    especie_info=datos['result']
                    name=especie_info['properties']['name']
                    uid=especie_info['uid']  
                    height=especie_info['properties']['average_height']
                    classification=especie_info['properties']['classification']
                    homeworld=especie_info['properties']['homeworld'] #url del planeta de origen
                    language =especie_info['properties']['language']
                    people=especie_info['properties']['people'] #esto es una lista de urls de los personajes que pertenecen a esa especie
                    
                    for personaje_url in people: #SUJETO A CAMBIOSSSSSSS
                        personaje_response = requests.get(personaje_url)
                        if personaje_response.status_code == 200:
                            personaje_id = personaje_url.split("/")[-1] #esto es para obtener el id del personaje
                            self.personaje_especie[personaje_id] = name #esto es para relacionar el id del personaje con la especie


                    response_homeworld = requests.get(homeworld)
                    if response_homeworld.status_code == 200:
                        datos_homeworld = response_homeworld.json()['result']['properties']
                        homeworld=datos_homeworld['name']

                    lista_personajes=[]
                    for personaje in people:
                        response_personaje = requests.get(personaje)
                        if response_personaje.status_code == 200:
                            datos_personaje = response_personaje.json()['result']['properties']
                            people = datos_personaje['name']
                            lista_personajes.append(people) #personajes que pertenecen a la especie
                     
                
                lista_episodios = [] #eps en los que aparece la especie
                for id_episodio in range (1,7):
                    '''print("Viendo especie: " + str(id_episodio))'''
                    id_episodio = str(id_episodio)
                    url_episodio = f"https://www.swapi.tech/api/films/{id_episodio}/"
                    response_episodio = requests.get(url_episodio)
                    if response_episodio.status_code == 200:
                        datos_episodio = response_episodio.json()['result']['properties']
                        if url in datos_episodio['species']:
                            """print("Conectando especie con episodio: " + str(id_episodio))"""
                            lista_episodios.append(datos_episodio['title'])


                
                nueva_especie = Especie(name, uid, height, classification, homeworld, language, lista_personajes,lista_episodios)
                self.especie_lista.append(nueva_especie)

    def crear_pelicula(self): 
        print("Cargando películas...")
        url = "https://swapi.dev/api/films/"
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()["results"]
            for pelicula in datos:
                title = pelicula["title"]
                episode = pelicula["episode_id"]
                director = pelicula["director"]
                release_date = pelicula["release_date"]
                opening_crawl = pelicula["opening_crawl"]
                nueva_pelicula = Pelicula(title, episode, release_date, opening_crawl, director)
                self.pelicula_lista.append(nueva_pelicula) 

             #quiero hacer que se muestren por orden de id de episodio
            self.pelicula_lista.sort(key=lambda x: x.episode_id)

    def crear_personaje(self):
        print("Cargango personajes...")
        for id_personaje in range(1, 83):
            id_personaje = str(id_personaje)
            url = f"https://www.swapi.tech/api/people/{id_personaje}"
            response_personaje = requests.get(url)
            if response_personaje.status_code == 200:
                datos_personaje = response_personaje.json()['result']['properties']
                nombre = datos_personaje['name']
                planeta_origen = datos_personaje['homeworld']
                genero = datos_personaje['gender']

                especie = self.personaje_especie.get(id_personaje)
                if especie is None:
                    especie = "Este personaje no pertenece a ninguna especie"

                if planeta_origen:  
                    response_planeta = requests.get(planeta_origen)
                    if response_planeta.status_code == 200:
                        datos_planeta = response_planeta.json()['result']['properties']
                        nombre_planeta = datos_planeta['name']

                        # Añade el personaje a la lista de personajes del planeta
                        if nombre_planeta in self.personaje_planeta:
                            self.personaje_planeta[nombre_planeta].append(nombre)
                        else:
                            self.personaje_planeta[nombre_planeta] = [nombre]
                    else:
                        nombre_planeta = "Desconocido"
                else:
                    nombre_planeta = "Desconocido"

                lista_episodios = self.obtener_episodios_de_personaje(id_personaje)
                episodios_str = ", ".join(lista_episodios)
               


                nuevo_personaje = Personaje(nombre, nombre_planeta, episodios_str, genero, especie, [], [])
                self.personaje_lista.append(nuevo_personaje)

            else:  # Si el personaje no existe o no se puede acceder
                continue
    
    def CSV_crear_personaje(self):
        archivo_personaje = pd.read_csv("characters.csv") 
    
        for i in range(len(archivo_personaje)):
            nombre = archivo_personaje.iloc[i, 1]
            planeta_origen = archivo_personaje.iloc[i, 10]
            genero = archivo_personaje.iloc[i, 3]
            especiet = archivo_personaje.iloc[i, 2]
            nuevo_personaje = Personaje(nombre, planeta_origen, 0,genero, especiet, 0, 0)
            self.CSV_personaje_lista.append(nuevo_personaje)

    def crear_nave(self):
        print("Cargando naves...")
        for nave_id in range(1, 37):
            nave_id = str(nave_id)
            url = f"https://www.swapi.tech/api/starships/{nave_id}"
            response_nave = requests.get(url)
            if response_nave.status_code == 200:
                datos_nave = response_nave.json()['result']['properties']
                nombre = datos_nave['name']
                longitud = datos_nave['length']
                carga = datos_nave['cargo_capacity']
                crew = datos_nave['crew']
                pasajeros = datos_nave['passengers']
                hiperdrive = datos_nave['hyperdrive_rating']
                MGLT = datos_nave['MGLT']
                vel_max = datos_nave['max_atmosphering_speed']
                costo = datos_nave['cost_in_credits']
                pilotos_nave = []
                for piloto_url in datos_nave['pilots']:
                    response_piloto = requests.get(piloto_url)
                    if response_piloto.status_code == 200:
                        datos_piloto = response_piloto.json()['result']['properties']
                        pilotos_nave.append(datos_piloto['name'])
                     
                self.nave_lista.append(Nave(nombre, longitud, carga, crew, pasajeros, pilotos_nave, hiperdrive, MGLT,vel_max,costo))
                
            else:
                continue

    def CSV_Crear_nave(self):
        archivo_nave = pd.read_csv("starships.csv") 
    
        for i in range(len(archivo_nave)):
            nombre = archivo_nave.iloc[i, 1]
            longitud = archivo_nave.iloc[i, 5]
            capacidad_carga = archivo_nave.iloc[i, 9]
            clasificacion_hiperimpulsor = archivo_nave.iloc[i, 11]
            mgl = archivo_nave.iloc[i, 12]
            vel_max = archivo_nave.iloc[i, 6]
            costo = archivo_nave.iloc[i, 4]
            nueva_nave = Nave(nombre, longitud, capacidad_carga, 0, 0, 0, clasificacion_hiperimpulsor, mgl, vel_max, costo)
            self.CSV_nave_lista.append(nueva_nave)       

    def crear_vehiculos(self):
        print("Creando vehículos...")
        for vehiculo_id in range(1, 40):
            vehiculo_id = str(vehiculo_id)
            url = f"https://www.swapi.tech/api/vehicles/{vehiculo_id}"
            response_vehiculo = requests.get(url)
            if response_vehiculo.status_code == 200:
                datos_vehiculo = response_vehiculo.json()['result']['properties']
                nombre = datos_vehiculo['name']
                longitude = datos_vehiculo['length']
                carga = datos_vehiculo['cargo_capacity']
                crew = datos_vehiculo['crew']
                pasajeros = datos_vehiculo['passengers']
                pilotos_vehiculo = []
                for piloto_url in datos_vehiculo['pilots']:
                    response_piloto = requests.get(piloto_url)
                    if response_piloto.status_code == 200:
                        datos_piloto = response_piloto.json()['result']['properties']
                        pilotos_vehiculo.append(datos_piloto['name'])
                self.vehiculos_lista.append(Vehiculo(nombre, longitude, carga, crew, pasajeros, pilotos_vehiculo))
            else:
                continue

    def obtener_episodios_de_personaje(self, id_personaje):
            episodios = []
            response_peliculas = requests.get("https://www.swapi.tech/api/films")
            if response_peliculas.status_code == 200:
                peliculas = response_peliculas.json()['result']
                for pelicula in peliculas:
                    personajes_en_pelicula = pelicula['properties']['characters']
                    if f"https://www.swapi.tech/api/people/{id_personaje}" in personajes_en_pelicula:
                        episodios.append(pelicula['properties']['title'])
            return episodios

    def crear_planeta(self):
        for id_planeta in range(1, 61):
                id_planeta = str(id_planeta)
                url = f"https://www.swapi.tech/api/planets/{id_planeta}" #esto solo dará el nombre, id y la url del planeta
                response_planeta = requests.get(url)

                if response_planeta.status_code == 200:
                    datos=response_planeta.json()
                    planeta_info=datos['result']
                    uid=planeta_info['uid']
                    name=planeta_info['properties']['name']
                    periodo_orbita=planeta_info['properties']['orbital_period']
                    periodo_rotacion=planeta_info['properties']['rotation_period']
                    habitantes=planeta_info['properties']['population'] #numero de habitantes
                    clima=planeta_info['properties']['climate']
                    #falta Nombre de los personajes que pertenecen a la especie y Nombre de los episodios en los que aparecen.

                    lista_planeta_en_episodio=[] #episodios en los que aparece el planeta
                    for id_episodio in range(1, 7):
                        id_episodio = str(id_episodio)
                        url_episodio = f"https://www.swapi.tech/api/films/{id_episodio}"
                        response_episodio = requests.get(url_episodio)
                        if response_episodio.status_code == 200:
    
                            datos_episodio = response_episodio.json()['result']['properties']
                            if url in datos_episodio['planets']:
                                lista_planeta_en_episodio.append(datos_episodio['title'])

                    lista_personajes_en_planeta = [] #personajes que pertenecen al planeta



                    nuevo_planeta = Planeta(uid, name, periodo_orbita, periodo_rotacion, habitantes, clima, lista_planeta_en_episodio, lista_personajes_en_planeta)
                    self.planeta_lista.append(nuevo_planeta)

    def CSV_Crear_planetas(self): 
        archivo_planeta = pd.read_csv("planets.csv") #se hace así
        for i in range(len(archivo_planeta)):
            nombre = archivo_planeta.iloc[i, 1]
            periodo_orbita = archivo_planeta.iloc[i, 4]
            periodo_rotacion = archivo_planeta.iloc[i, 3]
            habitantes = archivo_planeta.iloc[i, 6]
            clima = archivo_planeta.iloc[i, 8]
            nuevo_planeta = Planeta(0, nombre, periodo_orbita, periodo_rotacion, habitantes, clima, 0, 0)
            self.CSV_planeta_lista.append(nuevo_planeta) #ARREGLAR, FALTAN ARGUMENTOS

    def relacionar_personajes_con_planetas(self):
        for planeta in self.planeta_lista: #recorro la lista de planetas
            for persona in self.personaje_lista: #y recorro la de personajes
                if persona.planeta_origen == planeta.nombre: #si el homeplanet del personaje es igual al nombre del planeta
                    planeta.personajes.append(persona.nombre) #lo agrego >:D

    def relacionar_vehiculos_y_naves_con_personajes(self):
        for persona in self.personaje_lista:
            for vehiculo in self.vehiculos_lista:
                for piloto in vehiculo.pilotos:
                    if piloto == persona.nombre:
                        persona.vehiculos.append(vehiculo.nombre)
            if not persona.vehiculos:
                persona.vehiculos.append("Este personaje no maneja ningún vehículo")
            persona.vehiculos = ", ".join(persona.vehiculos)
                                          
        for persona in self.personaje_lista:
            for nave in self.nave_lista:
                for piloto in nave.pilotos:
                    if piloto == persona.nombre:
                        persona.naves.append(nave.nombre)
                    
            if not persona.naves:
                persona.naves.append("Este personaje no maneja ninguna nave")
            persona.naves = ", ".join(persona.naves)    

    def CSV_crear_arma(self):
        archivo_armas = pd.read_csv("weapons.csv") #se hace así
    
        for i in range(len(archivo_armas)):
            uid = archivo_armas.iloc[i, 0]
            nombre = archivo_armas.iloc[i, 1]
            modelo = archivo_armas.iloc[i, 2]
            tipo = archivo_armas.iloc[i, 6]
            descripcion = archivo_armas.iloc[i, 7]

            nueva_arma = Armas(uid, nombre, modelo, tipo, descripcion)
            self.csv_arma_lista.append(nueva_arma)

#A continuación se presentan los métodos para mostrar los menús y seleccionar las opciones del usuario


    def seleccionar_armas(self, num_armas):
        armas_seleccionadas = []
        while True:
            print("Menú de selección de armas:")
            for i, arma in enumerate(self.csv_arma_lista):
                print(f"{i + 1}. {arma.nombre}")
            print("0. Salir")
            
            opcion = input("Ingresa el número del arma que deseas seleccionar (1-60) o '0' para terminar: ")
            if opcion == "0":
                print("Saliendo del menú de armas...")
                break
            if opcion.isdigit():
                indice = int(opcion) - 1
                if 0 <= indice < len(self.csv_arma_lista):  # Verifica que el índice sea válido
                    if self.csv_arma_lista[indice] not in armas_seleccionadas:
                        armas_seleccionadas.append(self.csv_arma_lista[indice])
                        print(f"Has seleccionado el arma {self.csv_arma_lista[indice].nombre}.")
                    else:
                        print("Esta arma ya ha sido seleccionada. Elige otra.")
                else:
                    print("¡Opción inválida! Debes seleccionar un número entre 1 y 60.")
            else:
                print("¡Opción inválida! Introduce un número válido.")

            if len(armas_seleccionadas) >= num_armas:
                print(f"Has seleccionado el número requerido de armas: {num_armas}.")
                break

        return armas_seleccionadas

    def mostrar_menu_personajes(self):
        print("¡Hola viajero! aquí vas a poder escoger tus misiones")
        print("Menú de selección de personajes:")
        for i, personaje in enumerate(self.CSV_personaje_lista):
            print(f"{i + 1}. {personaje.nombre}")
        print(f"{len(self.CSV_personaje_lista) + 1}. Salir")

    def seleccionar_personajes(self, num_personajes):
        # Llama a CSV_crear_personaje para cargar personajes desde el CSV
        self.CSV_crear_personaje()  # personajes del csv_persona_lista
        personajes_seleccionados = []
        while True:
            print('Menú de selección de personajes:')
            for i, personaje in enumerate(self.CSV_personaje_lista):
                print(f"{i + 1}. {personaje.nombre}")
            print("0. Salir")
            
            opcion = input("Ingresa el número del personaje que deseas seleccionar (1-96) o '0' para terminar: ")
            if opcion == "0":
                print("Saliendo del menú de personajes...")
                break
            if opcion.isdigit():
                indice = int(opcion) - 1
                if 0 <= indice < len(self.CSV_personaje_lista):  # Verifica que el índice sea válido
                    if self.CSV_personaje_lista[indice] not in personajes_seleccionados:
                        personajes_seleccionados.append(self.CSV_personaje_lista[indice])
                        print(f"Has seleccionado al personaje {self.CSV_personaje_lista[indice].nombre}.")
                    else:
                        print("Este personaje ya ha sido seleccionado. Elige otro.")
                else:
                    print("¡Opción inválida! Debes seleccionar un número entre 1 y 96.")
            else:
                print("¡Opción inválida! Introduce un número válido.")

            if len(personajes_seleccionados) >= num_personajes:
                print(f"Has seleccionado el número requerido de personajes: {num_personajes}.")
                break

        return personajes_seleccionados

    def mostrar_menu_planetas(self):
        print("Aquí podrás seleccionar el nombre del planeta para tu batalla:")
        for i, planeta in enumerate(self.CSV_planeta_lista):
            print(f"{i + 1}.- {planeta.nombre}")
        print("0.- Salir")

    def seleccionar_planeta(self):
        while True:
            self.mostrar_menu_planetas()
            opcion_p = input("\nIngresa aquí el número del planeta al que quieres viajar, o introduce '0' para salir: ")
            
            if opcion_p == "0":
                print("\nSaliendo del menú...")
                return None  # Salir y devolver None
            
            if opcion_p.isdigit():
                indice = int(opcion_p) - 1
                if 0 <= indice < len(self.CSV_planeta_lista):  # Verifica que el índice sea válido
                    planeta_seleccionado = self.CSV_planeta_lista[indice]
                    print(f"\nHas seleccionado el planeta {planeta_seleccionado.nombre}")
                    return planeta_seleccionado  # Devolver el planeta seleccionado
                else:
                    print("¡Opción inválida! Debes seleccionar un número entre 1 y 13.")
            else:
                print("¡Opción inválida! Introduce un número válido.")

    def mostrar_menu_naves(self):
        print("Aquí podrás seleccionar el nombre de la nave en la que quieres viajar:")
        for i, nave in enumerate(self.CSV_nave_lista):
            print(f"{i + 1}.- {nave.nombre}")
        print("0.- Salir")

    def seleccionar_nave(self):
        self.CSV_Crear_nave()
        while True:
            self.mostrar_menu_naves()
            opcion_n = input("Ingresa aquí el número de la nave al que quieres viajar, o introduce '0' para salir: ")
            
            if opcion_n == "0":
                print("Saliendo del menú...")
                return None  # Salir y devolver None
            
            if opcion_n.isdigit():
                indice = int(opcion_n) - 1
                if 0 <= indice < len(self.CSV_nave_lista):  # Verifica que el índice sea válido
                    nave_seleccionada = self.CSV_nave_lista[indice]
                    print(f"Has seleccionado la nave {nave_seleccionada.nombre}")
                    return nave_seleccionada  # Devolver la nave seleccionada
                else:
                    print("¡Opción inválida! Debes seleccionar un número entre 1 y 60.")
            else:
                print("¡Opción inválida! Introduce un número válido.")

    def crear_mision(self, usuario):  
        if len(self.mision_lista) >= 5:  # hasta 5 misiones
            print("Ya has alcanzado el límite de 5 misiones.")
            return

        # Selección de planeta
        print("Indíqueme el destino al que quiere ir:")
        planeta_seleccionado = self.seleccionar_planeta()
        if not planeta_seleccionado:  
            print("No se seleccionó ningún planeta. Cancela la creación de la misión.")
            return

        # Selección de nave
        print("Indíqueme la nave que quiere usar:")
        nave_seleccionada = self.seleccionar_nave()
        if not nave_seleccionada: 
            print("No se seleccionó ninguna nave. Cancela la creación de la misión.")
            return

        # Selección de personajes
        personajes = self.seleccionar_personajes(7)
        if not personajes:  
            print("Debes seleccionar al menos un personaje. Cancela la creación de la misión.")
            return

        # Selección de armas
        armas = self.seleccionar_armas(7)

        # Crear la misión
        nombre = f"batalla de {planeta_seleccionado.nombre}"
        nueva_mision = Mision(nombre, planeta_seleccionado, nave_seleccionada, personajes, armas)    
        usuario.mision_lista.append(nueva_mision)

        print(f"Misión '{nombre}' creada exitosamente.")

    def modificar_misiones(self):
        while True:
            print("\nSelecciona la misión que deseas modificar:")
            for i, mision in enumerate(self.mision_lista):
                print(f"{i + 1}. {mision.nombre}")
            
            opcion = input("Ingresa el número de la misión que deseas modificar o 'salir' para terminar: ")
            if opcion.isdigit() and 1 <= int(opcion) <= len(self.mision_lista):
                mision_seleccionada = self.mision_lista[int(opcion) - 1]
                print(f"\nModificando la misión: {mision_seleccionada.nombre}")

                # Menú para modificar atributos
                while True:
                    print("\n¿Qué deseas modificar?")
                    print("1. Personajes")
                    print("2. Nave")
                    print("3. Armas")
                    print("4. Planeta")
                    print("5. Salir de la modificación")

                    sub_opcion = input("Selecciona una opción: ")
                    if sub_opcion == "1":
                        personajes_nuevos = self.seleccionar_personajes()
                        if personajes_nuevos:
                            mision_seleccionada.personajes = personajes_nuevos
                            print("Personajes actualizados.")
                        else:
                            print("No se seleccionaron personajes.")

                    elif sub_opcion == "2":
                        nave_nueva = self.seleccionar_nave()
                        if nave_nueva:
                            mision_seleccionada.nave = nave_nueva
                            print("Nave actualizada.")
                        else:
                            print("No se seleccionó ninguna nave.")

                    elif sub_opcion == "3":
                        armas_nuevas = self.seleccionar_armas()  # O especificar un límite si es necesario
                        if armas_nuevas:
                            mision_seleccionada.armas = armas_nuevas
                            print("Armas actualizadas.")
                        else:
                            print("No se seleccionaron armas.")

                    elif sub_opcion == "4":
                        planeta_nuevo = self.seleccionar_planeta()
                        if planeta_nuevo:
                            mision_seleccionada.planeta = planeta_nuevo
                            print("Planeta actualizado.")
                        else:
                            print("No se seleccionó ningún planeta.")

                    elif sub_opcion == "5":
                        print("Saliendo del menú de modificaciones...")
                        break

                    else:
                        print("Opción inválida. Intenta de nuevo.")
            
            elif opcion.lower() == "salir":
                print("Saliendo del menú de modificaciones...")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")

    def guardar_misiones(self):
        with open("misiones.txt", "w") as f:
            for mision in self.mision_lista:
                mision:Mision
                # Cambiar la forma en que se guardan los personajes y armas
                personajes_nombres = [p.nombre for p in mision.personajes]  # Extraer los nombres de los personajes
                armas_nombres = [arma.nombre for arma in mision.armas_seleccionadas]  # Extraer los nombres de las armas
                f.write(f"{mision.nombre},{mision.planeta_seleccionado.nombre},{mision.nave_seleccionada.nombre},{','.join(personajes_nombres)},{','.join(armas_nombres)}\n")
        print("Misiones guardadas exitosamente.")

    def cargar_misiones(self):
        try:
            with open("misiones.txt", "r") as f:
                for line in f:
                    nombre, planeta_nombre, nave_nombre, personajes_str, armas_str = line.strip().split(',')
                    personajes = personajes_str.split(',')
                    armas = armas_str.split(',')
                    
                    # Aquí debes encontrar el objeto planeta y nave por su nombre
                    planeta = next((p for p in self.planeta_lista if p.nombre == planeta_nombre), None)
                    nave = next((n for n in self.nave_lista if n.nombre == nave_nombre), None)
                    
                    if planeta and nave:
                        mision = Mision(nombre, planeta, nave, armas, personajes)
                        self.mision_lista.append(mision)
                    else:
                        print(f"Error al cargar la misión '{nombre}': planeta o nave no encontrados.")
            print("Misiones cargadas exitosamente.")
        except FileNotFoundError:
            print("El archivo de misiones no se encontró.")

    def visualizar_misiones(self):
        if not self.mision_lista:
            print("No tienes misiones creadas.")
            return

        print("Tus misiones:")
        for i, mision in enumerate(self.mision_lista):
            print(f"{i + 1}. {mision.nombre}")

        opcion = input("Selecciona el número de la misión para ver detalles o 'salir' para volver: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(self.mision_lista):
            mision = self.mision_lista[int(opcion) - 1]
            print(f"Detalles de la misión '{mision.nombre}':")
            print(f"Planeta: {mision.planeta_seleccionado.nombre}")
            print(f"Nave: {mision.nave_seleccionada.nombre}")
            print(f"Personajes: {', '.join([p.nombre for p in mision.personajes])}")
            print(f"Armas: {', '.join([arma.nombre for arma in mision.armas_seleccionadas])}")  # Cambiar armas_seleccionadas a armas
        elif opcion.lower() == "salir":
            print("Volviendo al menú de misiones...")
        else:
            print("Opción inválida.")       