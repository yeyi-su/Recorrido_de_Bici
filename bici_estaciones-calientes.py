import pandas as pd # importamos la bilblioteca pandas

archivo_csv = 'trips_2023.csv'#Definimos el archivo 
df = pd.read_csv(archivo_csv)#Utilizamos read_csv para cargar los datos del archivo csv en un DataFrame('df') estructura de datos.

df['fecha_origen_recorrido'] = pd.to_datetime(df['fecha_origen_recorrido'])#Convierte la columna fecha_origen_recorrido en objetos de tipo datetime. Es útil para realizar operaciones relacionadas con fechas y horas.

manana = (df['fecha_origen_recorrido'].dt.hour >= 6) & (df['fecha_origen_recorrido'].dt.hour <= 11)#Se crea un DataFrame para filtrar donde fecha_origen_recorrido está entre 06:00 y 11:59
recorridos_en_la_manana = df[manana]#Se crea un DataFrame recorridos_en_la_manana que contiene solo las filas que cumplen ese criterios.

frecuencia_de_estaciones = recorridos_en_la_manana['nombre_estacion_origen'].value_counts()#Estalinea es paracontar la frecuencia de cada valor único de la columna nombre_estacion_origen.

print("Estaciones más recorridos en la mañana:")#Imprime un encabezado
print(frecuencia_de_estaciones.head(3))#Imprime las tres estaciones de origen con más recorridos en la mañana.
