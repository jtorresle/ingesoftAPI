from fastapi import FastAPI
from routers.users import user
from routers.propiedad import propiedad
app = FastAPI()

app.include_router(user)
app.include_router(propiedad)