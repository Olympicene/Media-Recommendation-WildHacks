import requests
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
THEMOVEDB_API_KEY = os.getenv('THEMOVEDB_API_KEY')


app = FastAPI()

@app.get("/rand")
def read_root():

    headers = {
        "Authorization": f"Bearer {THEMOVEDB_API_KEY}",
        "Content-Type": "application/json;charset=utf-8",
    }

    response = requests.get('https://api.themoviedb.org/3/movie/76341', headers=headers)
    print(response)

    return {
        "Type1": "x1",
        "ID1": "y1",
        "Typ2": "x2",
        "ID2": "y2",
        "score": 100,
        "total": 1000,
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}