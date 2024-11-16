from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import numpy as np
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


model = joblib.load("app/models/model.joblib")


class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(requests: HouseData):
    features = np.array([[requests.MedInc,requests.HouseAge,requests.AveRooms,
                          requests.AveBedrms,requests.Population,requests.AveOccup,
                          requests.Latitude,
                          requests.Longitude]])
    prediction = model.predict(features)

    return {"predicted_house_price":prediction[0]*10e5}



