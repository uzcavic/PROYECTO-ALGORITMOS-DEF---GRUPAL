import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def crear_arma():
    # Leer el archivo CSV
    archivo_armas = pd.read_csv("weapons.csv")
    
    # Obtener estadísticas descriptivas
    estadisticas = archivo_armas.describe()
    
    # Mostrar las estadísticas
    print(estadisticas)

# Llamar a la función
crear_arma()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def crear_grafico():
    # Leer el archivo CSV
    archivo_armas = pd.read_csv("weapons.csv")
    
    # Limpiar los nombres de las columnas
    archivo_armas.columns = archivo_armas.columns.str.strip()
    print(archivo_armas.model) 
    # Mostrar las columnas del DataFrame
    print(archivo_armas.columns)
    
    # Crear un gráfico de barras del daño de las armas
    plt.figure(figsize=(10, 6))
    sns.barplot(x='nombre', y='daño', data=archivo_armas)  # Asegúrate de que estos nombres son correctos
    
    # Añadir título y etiquetas
    plt.title('Daño de las Armas')
    plt.xlabel('Nombre de la Arma')
    plt.ylabel('Daño')
    
    # Rotar las etiquetas del eje x para mejor legibilidad
    plt.xticks(rotation=45)
    
    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

# Llamar a la función para crear el gráfico
crear_grafico()