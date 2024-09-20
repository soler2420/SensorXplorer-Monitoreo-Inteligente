from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de datos para el sensor
class Sensor(BaseModel):
    id: int
    nombre: str
    temperatura: float
    humedad: float
    tiempo: float  # Este campo es requerido

# Modelo de configuración
class Configuracion(BaseModel):
    temp_min: float
    temp_max: float
    humedad_min: float
    humedad_max: float

# Lista para almacenar los datos de los sensores
sensores_data = []

@app.post("/guardar_datos")
async def guardar_datos(sensores: List[Sensor]):
    global sensores_data
    try:
        # Agregar los nuevos datos a la lista
        sensores_data.extend(sensores)
        return {"mensaje": "Datos guardados exitosamente", "datos": sensores}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/datos")
async def obtener_datos():
    return {"datos": sensores_data}

# Nueva ruta para la configuración
@app.get("/configuracion")
async def obtener_configuracion():
    configuracion = Configuracion(
        temp_min=7.0,
        temp_max=7.5,
        humedad_min=60,
        humedad_max=80
    )
    return configuracion

@app.get("/")
async def root():
    return {"mensaje": "API funcionando"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




