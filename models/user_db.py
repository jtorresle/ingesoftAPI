from sqlalchemy import FLOAT, INTEGER, Column, Integer, Table, String, SMALLINT
from config.db import meta, engine

users = Table("users",meta 
            ,Column("id",Integer,primary_key=True)
            ,Column("name",String(255))
            ,Column("email", String(255))
            ,Column("password", String(255)))
propiedades = Table("propiedades", meta
                    ,Column("Id",String(250),primary_key=True)
                    ,Column("Tipo_Propiedad",String(250))
                    ,Column("Area",FLOAT)
                    ,Column("N_Habitaciones",SMALLINT)
                    ,Column("N_Baños",SMALLINT)
                    ,Column("Administración",INTEGER)
                    ,Column("N_Parqueaderos",SMALLINT)
                    ,Column("Estrato",String(10))
                    ,Column('Descripcion',String(1000))
                    ,Column('Precio_Arriendo',INTEGER)
                    ,Column('Direccion',String(200))
                    )
images_propiedades = Table("images_propiedades",meta
                    ,Column("Id", String(500))
                    ,Column("URL", String(500)))
meta.create_all(engine)

