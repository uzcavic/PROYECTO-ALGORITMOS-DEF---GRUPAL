import requests
from Pelicula import Pelicula
from Especie import Especie
from Personaje import Personaje
from Planeta import Planeta
from Nave import Nave, Vehiculo
import matplotlib.pyplot as plt #para instalar esta libreria se habre una nueva terminal, aparece en los tres puntos de arriba, ya abierto colocar "pip install matplotlib" y listo 
import statistics
import pandas as pd
from statistics import mean, multimode

class APP:
    especie_lista = []
    pelicula_lista = []
    personaje_lista = []
    planeta_lista = []
    nave_lista = []
    vehiculos_lista = []
    personaje_especie = {}
    personaje_nave = {} 
    personaje_planeta = {}    
    
    
    def start(self):
            
            print('Cargando datos...')
            self.crear_pelicula() 
            self.crear_especies() 
            self.crear_planeta() 
            
            self.crear_personaje() 

            self.relacionar_personajes_con_planetas()
            '''for  planeta in self.planeta_lista:
                planeta.showPlaneta()'''

            self.crear_nave() 
            '''print("NAVES")
            for nave in self.nave_lista:
                nave.showNave()'''
            '''print("Vehículos")'''
            self.crear_vehiculos() 
            '''for vehiculo in self.vehiculos_lista:
                vehiculo.showVehiculo()'''
            self.relacionar_vehiculos_y_naves_con_personajes()
            '''for personaje in self.personaje_lista:
                personaje.showPersonaje()'''
            


            while True:
                print("""Bienvenido viajero, indique qué desea saber del universo de Star Wars
        1. Ver lista de peliculas
        2. Ver lista de especies
        3. Ver lista de planetas
        4. Buscar personaje
        5. Gráficos de la población de los planetas
        6. Gráficos diferenciadores de las naves
        7. Estadísticas básicas sobre valores de la nave
        8. Menú de misiones                    
        9. Terminar el programa""")
                opcion = input("---> ")
                if opcion =="1":
                    contador=1
                    for pelicula in self.pelicula_lista:
                        pelicula:Pelicula
                        print(f"Pelicula N°{contador}\n")
                        pelicula.showPelicula()
                        contador+=1 
                elif opcion =="2":
                    contador=1
                    for especie in self.especie_lista:
                        especie:Especie
                        print(f"Especie N°{contador}\n")
                        especie.showEspecie()
                        contador+=1
                elif opcion =="3":
                    contador=1
                    for planeta in self.planeta_lista:
                        planeta:Planeta
                        print(f"Planeta N°{contador}\n")
                        planeta.showPlaneta()
                        contador+=1 
                elif opcion =="4":
                    for personaje in self.personaje_lista:
                        personaje:Personaje
                        personaje.showPersonaje()                         
                elif opcion =="5":
                    self.grafica_planetas()
                elif opcion =="6":
                    self.Grafica_nave()  
                elif opcion =="7":
                    self.Estadistica_nave()    
                elif opcion =="9":
                    print("""Gracias y que la fuerza te acompañe
                        
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢀⣤⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣟⠛⠛⠛⠛⠛⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⢠⣿⣿⣿⣿⠿⣿⣿⣿⣿⡀⠀⠀⢸⣿⣿⣿⣿⡏⠉⠉⢉⣿⣿⣿⣿⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⡀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣾⣿⣿⣿⡟⠀⢻⣿⣿⣿⣧⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀
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
                else:
                    print("Opción inválida, intente de nuevo")


    def grafica_planetas(self):            
            nombre=[]
            poblacion=[]
            print(self.planeta_lista)
            for planeta in self.planeta_lista:
                planeta:Planeta
                if planeta.habitantes == "unknown":
                    nombre.append(planeta.nombre)
                    poblacion.append(0)
                else:
                    nombre.append(planeta.nombre)
                    poblacion.append(float(planeta.habitantes))
            print(nombre)
            print(poblacion)    
            plt.bar(nombre,poblacion, width=0.6)
            plt.title('Poblacion de cada planeta')
            plt.xlabel('Nombre de planetas')
            plt.ylabel('Poblacion')
            plt.xticks(rotation=90)
            plt.show()
                    
    def Grafica_nave(self):        
        carga =[]
        hiperpulsor=[]
        mglt=[]
        nombres=[]
        longtudes=[]
        for nave in self.nave_lista:
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
                plt.title("longitudes des naves") 
                plt.bar(nombres,longtudes,label=("longitud"),color="blue",width=0.6)   
                plt.xlabel('Nombre de naves')
                plt.ylabel('magnitud')
                plt.xticks(rotation=90)         
                plt.legend()
                plt.show()
                continue
             elif Estadi_menu=="2":
                #plt.subplot(222)
                plt.bar(nombres,carga,label=("carga"),color="red",width=0.6)   
                plt.title("carga de naves")
                plt.xlabel('Nombre de naves')
                plt.ylabel('magnitud')    
                plt.xticks(rotation=90)         
                plt.legend() 
                plt.show()
                continue 
             elif Estadi_menu=="3":
               #plt.subplot(223)
                plt.bar(nombres,hiperpulsor,label=("hiperpulso"),color="green",width=0.6)   
                plt.title("hiperpulsor de naves") 
                plt.xlabel('Nombre de naves')
                plt.ylabel('magnitud')   
                plt.xticks(rotation=90)         
                plt.legend()  
                plt.show()
                continue
             elif Estadi_menu=="4":
               #plt.subplot(224)
                plt.bar(nombres,mglt,label=("MGLB"),color="cyan",width=0.6)   
                plt.title("MGLT de naves")  
                plt.xlabel('Nombre de naves')
                plt.ylabel('magnitud')  
                plt.xticks(rotation=90)         
                plt.legend() 
                plt.show()
                continue
             elif Estadi_menu=="5":
                  break
             else:
                  print("valor invalido\n") 

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
        for nave in self.nave_lista:
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
        personaje_planeta = {} 
        for id_personaje in range(1, 83):
            id_personaje = str(id_personaje)
            print("Viendo personaje: " + str(id_personaje))
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
                nuevo_personaje = Personaje(nombre, nombre_planeta, lista_episodios, genero, especie, [], [])
                self.personaje_lista.append(nuevo_personaje)

            else:  # Si el personaje no existe o no se puede acceder
                continue

    def crear_nave(self):
        for nave_id in range(1, 37):
            nave_id = str(nave_id)
            print("Viendo nave: " + str(nave_id))
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

    def crear_vehiculos(self):
        for vehiculo_id in range(1, 40):
            vehiculo_id = str(vehiculo_id)
            print("Viendo vehiculo: " + str(vehiculo_id))
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
                            print("Viendo episodio: " + str(id_episodio))
                            datos_episodio = response_episodio.json()['result']['properties']
                            if url in datos_episodio['planets']:
                                lista_planeta_en_episodio.append(datos_episodio['title'])

                    lista_personajes_en_planeta = [] #personajes que pertenecen al planeta



                    nuevo_planeta = Planeta(uid, name, periodo_orbita, periodo_rotacion, habitantes, clima, lista_planeta_en_episodio, lista_personajes_en_planeta)
                    self.planeta_lista.append(nuevo_planeta)

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

    def crear_arma(self):
    
#Aquí va el menú de las misiones
