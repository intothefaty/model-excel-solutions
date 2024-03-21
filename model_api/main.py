from fastapi import FastAPI, HTTPException, Body
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import pandas as pd
import models_excels.application

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  # Vue.js uygulamasının çalıştığı adres
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.post("/veri_al/")
async def veri_al(data: Dict[Any, Any]):
    # Listeyi bir DataFrame'e dönüştürelim
    df = pd.DataFrame(data['data'])

    # NaN değerlerini 0 ile değiştirelim
    df = df.fillna(0)

    df = models_excels.application.run_all(df)

    # DataFrame'i tekrar bir liste haline getirelim
    data = df.to_dict(orient='records')

    return data
