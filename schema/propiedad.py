from typing import Optional
from pydantic import BaseModel

class Propiedad(BaseModel):
    Id: Optional[str] = None
    Tipo_Propiedad: Optional[str] = None
    Area: Optional[float] = None
    N_Habitaciones: Optional[int] = None
    N_Baños: Optional[int] = None
    Administración: Optional[float] = None
    N_Parqueaderos: Optional[int] = None
    Estrato: Optional[int] = None
    Descripcion: Optional[str] = None
    Precio_Arriendo: Optional[float] = None
    Direccion: Optional[str] = None
    


