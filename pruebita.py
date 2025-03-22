import sqlalchemy
from config.db import conn
from models.user_db import propiedades, images_propiedades
import pandas as pd
from sqlalchemy.sql import select
import time
inicio = time.time()
datos_propiedades = conn.execute(propiedades.select()).fetchall()
imagenes = conn.execute(images_propiedades.select()).fetchall()

# datos_propiedades = conn.execute(propiedades.join(images_propiedades,propiedades.c.Id==images_propiedades.c.Id))

propiedades_columns_names = propiedades.columns.keys()
lista_de_propiedades = [dict(zip(propiedades_columns_names, fila)) for fila in datos_propiedades]

images_columns_names =images_propiedades.columns.keys()
lista_de_imagenes = [dict(zip(images_columns_names, fila)) for fila in imagenes]

# lista_de_propiedades[1]["images"] = {"image1":"hola"}
# print(lista_de_propiedades[1]["images"]["image1"])
# lista_de_imagenes[1].update(lista_de_propiedades)

df = pd.DataFrame(lista_de_imagenes)
df2 = df.groupby("Id")["URL"].agg(list).reset_index()
df1 = pd.DataFrame(lista_de_propiedades)
result = pd.merge(df1,df2,how='inner',on='Id')
result['Images'] = result['URL'].apply(lambda urls: {'Image{}'.format(i + 1): url for i, url in enumerate(urls)})
# result = pd.merge(df,df1,on='Id',how="inner")
# print(lista_de_propiedades)
# print(lista_de_imagenes)
result.drop(['URL'],inplace=True,axis=1)
resultado = result.to_dict(orient='records')
# print(result.columns)
# print(len(df2.index))
# print(len(df1))
# print(df2)
# print(resultado)
fin = time.time()
print(fin-inicio)
diccion = {"hola": {"hola1": 3,"hola2" : 4}}


