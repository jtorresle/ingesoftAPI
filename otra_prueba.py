"""
otra_prueba.py

Este script realiza una consulta a la base de datos para obtener información de propiedades
inmobiliarias junto con sus imágenes. Usa SQLAlchemy para interactuar con la base de datos y
pandas para procesar y estructurar los datos en un formato amigable (lista de diccionarios).

Autor: [Tu nombre]
Fecha: [Fecha actual]
"""

# Importaciones necesarias
from re import T  # ❌ No se usa en el código. Puede eliminarse.
import sqlalchemy
from config.db import conn  # Conexión a la base de datos
from models.user_db import propiedades, images_propiedades  # Tablas SQLAlchemy
import pandas as pd
from sqlalchemy.sql import select
import time

# Medimos el tiempo de ejecución del proceso
inicio = time.time()

# Consulta SQL: JOIN entre propiedades e imágenes según el Id de la propiedad
datos_propiedades = conn.execute(
    select(propiedades.join(images_propiedades, propiedades.c.Id == images_propiedades.c.Id))
).fetchall()

# Convertimos el resultado en un DataFrame de pandas
df = pd.DataFrame(datos_propiedades)

# Eliminamos la columna duplicada de Id (resultado del join)
df.drop('Id_1', inplace=True, axis=1)

# Agrupamos por las columnas de propiedad, unificando las URLs de imágenes como una lista
df2 = df.groupby([
    'Id', 'Tipo_Propiedad', 'Area', 'N_Habitaciones', 'N_Baños',
    'Administración', 'N_Parqueaderos', 'Estrato', 'Descripcion',
    'Precio_Arriendo', 'Direccion'
])["URL"].agg(list).reset_index()

# Convertimos la lista de URLs en un diccionario tipo: {"Image1": url1, "Image2": url2, ...}
df2['Images'] = df2['URL'].apply(
    lambda urls: {'Image{}'.format(i + 1): url for i, url in enumerate(urls)}
)

# Eliminamos la columna original de URL
df2.drop('URL', inplace=True, axis=1)

# Resultado final: lista de diccionarios, uno por propiedad, con sus imágenes agrupadas
resultado = df2.to_dict(orient='records')

# Imprimimos el tiempo total de ejecución del script
fin = time.time()
print(fin - inicio)
