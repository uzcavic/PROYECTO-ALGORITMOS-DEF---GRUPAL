import requests
from Usuario import Usuario
from Armas import Armas
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
    CSV_planeta_lista = []
    nave_lista=[]
    CSV_nave_lista = []
    vehiculos_lista = []
    arma_lista = [] 
    misiones_usuario_lista = []
    personaje_especie = {}
    personaje_nave = {} 
    personaje_planeta = {}    
    
    
    def start(self):
            self.CSV_Crear_nave()
            self.CSV_Crear_planetas()
            self.crear_arma()
            '''for arma in self.arma_lista:
                arma.showArmas()'''
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
            self.mostrar_menu()

            


            while True: #registrar usuario primero 

                print("""Bienvenido viajero, indique qué desea saber del universo de Star Wars
                        1. Registrar usuario
                        2. Ver lista de peliculas
                        3. Ver lista de especies
                        4. Ver lista de planetas
                        5. Buscar personaje
                        6. Gráficos de la población de los planetas
                        7. Gráficos diferenciadores de las naves
                        8. Estadísticas básicas sobre valores de la nave
                        9. Menú de misiones                    
                        10. Terminar el programa""")
                opcion = input("---> ")
                if opcion == "1":
                    nombre = input("Ingrese su nombre: ")
                    uid= input("Ingrese su ID: ")


                elif opcion =="2":
                    contador=1
                    for pelicula in self.pelicula_lista:
                        pelicula:Pelicula
                        print(f"Pelicula N°{contador}\n")
                        pelicula.showPelicula()
                        contador+=1 
                elif opcion =="3":
                    contador=1
                    for especie in self.especie_lista:
                        especie:Especie
                        print(f"Especie N°{contador}\n")
                        especie.showEspecie()
                        contador+=1
                elif opcion =="4":
                    contador=1
                    for planeta in self.planeta_lista:
                        planeta:Planeta
                        print(f"Planeta N°{contador}\n")
                        planeta.showPlaneta()
                        contador+=1 
                elif opcion =="5":
                    for personaje in self.personaje_lista:
                        personaje:Personaje
                        personaje.showPersonaje()                         
                elif opcion =="6":
                    self.grafica_planetas()
                elif opcion =="7":
                    self.Grafica_nave()  
                elif opcion =="8":
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
            for planeta in self.CSV_planeta_lista:
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

    def CSV_Crear_nave(self):
        archivo_nave = pd.read_csv("starships.csv") #se hace así
    
        for i in range(len(archivo_nave)):
            nombre = archivo_nave.iloc[i][1]
            longitud = archivo_nave.iloc[i][5]
            capacidad_carga = archivo_nave.iloc[i][9]
            clasificacion_hiperimpulsor = archivo_nave.iloc[i][11]
            mgl = archivo_nave.iloc[i][12]
            vel_max = archivo_nave.iloc[i][6]
            costo = archivo_nave.iloc[i][4]
            nueva_nave = Nave(nombre, longitud, capacidad_carga, clasificacion_hiperimpulsor, mgl,vel_max,costo)
            self.CSV_nave_lista.append(nueva_nave)        

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

    def CSV_Crear_planetas(self): 
        archivo_planeta = pd.read_csv("planets.csv") #se hace así
        for i in range(len(archivo_planeta)):
            nombre = archivo_planeta.iloc[i][1]
            periodo_orbita = archivo_planeta.iloc[i][4]
            periodo_rotacion = archivo_planeta.iloc[i][3]
            habitantes = archivo_planeta.iloc[i][6]
            clima = archivo_planeta.iloc[i][8]
            nuevo_planeta = Planeta(nombre, periodo_orbita, periodo_rotacion, habitantes, clima)
            self.CSV_planeta_lista.append(nuevo_planeta)

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
        archivo_armas = pd.read_csv("weapons.csv") #se hace así
    
        for i in range(len(archivo_armas)):
            uid = archivo_armas.iloc[i][0]
            nombre = archivo_armas.iloc[i][1]
            modelo = archivo_armas.iloc[i][2]
            tipo = archivo_armas.iloc[i][6]
            descripcion = archivo_armas.iloc[i][7]

            nueva_arma = Armas(uid, nombre, modelo, tipo, descripcion)
            self.arma_lista.append(nueva_arma)

#Aquí va el menú de las misiones
#Menú para el personaje

    def mostrar_menu_personajes(self):
        print("¡Hola viajero! aquí vas a poder escoger tus misiones")
        print("Menú de selección de personajes:")
        for i, personaje in enumerate(self.personajes):
            print(f"{i + 1}. {personaje.nombre}")
        print(f"{len(self.personajes) + 1}. Salir")

    def seleccionar_personajes(self):
        personajes_seleccionados = []
        while True:
            self.mostrar_menu_personajes()
            opcion_pe = input("Ingresa el número del personaje que deseas seleccionar (7 max) o 'salir' para terminar: ")

            if opcion_pe == str(len(self.personajes) + 1):
                print("Saliendo del menú...")
                break
            if opcion_pe.isdigit():
                indice = int(opcion_pe) - 1
                if 0 <= indice < len(self.personajes):
                    if self.personajes[indice] not in personajes_seleccionados:
                        personajes_seleccionados.append(self.personajes[indice])
                        print(f"Has seleccionado al personaje {self.personajes[indice].nombre}.")
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
                if 0 <= indice < len(self.planetas):
                    planeta_seleccionado = self.planetas[indice]
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
        for i, nave in enumerate(self.naves):
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
            print(f"Perfecto, has elegido la nave {nave_seleccionada.nombre}.")
        else:
            print("No has seleccionado ninguna nave.")

    def crear_mision(self):  
        #poner while
        print("indiqueme el destino al que quiere ir")
        index=1
        for planeta in self.planeta_lista:
            planeta:Planeta
            print(f"{index}-{planeta.nombre}")
            index+=1
        elccion = int(input("--> "))
        planeta_1 = self.planeta_lista[elccion-1]
#poner while
        print("indiqueme la nave que quiere usar")
        index=1
        for nave in self.nave_lista:
            nave:Nave
            print(f"{index}-{nave.nombre}")
            index+=1
        elccion = int(input("--> "))
        nave_1 = self.nave_lista[elccion-1]

        personajes=[]
        elige=True
        while len(personajes)<7 and elige==True:
            print("indiqueme el personaje que quiere usar ")
            index=1
            for personaje in self.personaje_lista:
                personaje:Personaje
                print(f"{index}-{personaje.nombre}")
                index+=1
            elccion = int(input("--> "))
            personaje = self.personaje_lista[elccion-1]
            personajes.append(personaje)
            
            while True:
                otro=input("""Quieres elegir a otro personaje
        1. si
        2. no 
---> """)
                if otro=="1":
                    break
                elif otro=="2":
                    elige=False
                    break
                else:
                    print("opcion invalida")
        armas=[]
        while len(armas)!=len(personajes):
            print("indiqueme el personaje que quiere usar ")
            index=1
            for arma in self.arma_lista:
                arma:Armas
                print(f"{index}-{arma.nombre}")
                index+=1
            elccion = int(input("--> "))
            arm = self.arma_lista[elccion-1]
            personajes.append(arm)
            print("Elige la misma cantidad de armas que de personajes escogigos\n")
