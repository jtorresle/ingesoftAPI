from fastapi import APIRouter, Response
from config.db import conn
from models.user_db import propiedades, images_propiedades
from schema.propiedad import Propiedad
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.sql import select
import pandas as pd

propiedad = APIRouter()

@propiedad.get("/propiedad")
def get_propiedad():
    datos_propiedades = conn.execute(select(propiedades.join(images_propiedades,propiedades.c.Id==images_propiedades.c.Id))).fetchall()
    df = pd.DataFrame(datos_propiedades)
    df.drop('Id_1',inplace=True,axis=1)
    print(df.columns)
    df2 = df.groupby(['Id', 'Tipo_Propiedad', 'Area', 'N_Habitaciones', 'N_Baños',
        'Administración', 'N_Parqueaderos', 'Estrato', 'Descripcion',
        'Precio_Arriendo', 'Direccion'])["URL"].agg(list).reset_index()

    df2['Images'] = df2['URL'].apply(lambda urls: {'Image{}'.format(i + 1): url for i, url in enumerate(urls)})
    df2.drop('URL',inplace=True,axis=1)
    resultado = df2.to_dict(orient='records')
    return resultado

@propiedad.post("/propiedad")
def create_user(arriendo: Propiedad):
    new_user = arriendo.model_dump(exclude_unset=True)
    result = conn.execute(propiedades.insert().values(**new_user))
    data = conn.execute(propiedades.select().where(propiedades.c.Id == result.lastrowid)).first()   
    return data._asdict()

@propiedad.delete("/propiedad/{id}")
def delete_propiedad(id):
    conn.execute(propiedades.delete().where(propiedades.c.Id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@propiedad.put('/propiedad/{id}')
def update_user(id: str, arriendo: Propiedad):
    values = arriendo.model_dump(exclude_unset=True)
    conn.execute(propiedades.update().values(**values).where(propiedades.c.Id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)