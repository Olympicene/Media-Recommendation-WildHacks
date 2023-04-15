import requests
import os
import random
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
THEMOVIEDB_API_KEY = os.getenv('THEMOVIEDB_API_KEY')

# UGLY CONTSTANTS
MAX_MOVIE_ID = 1113623
MAX_TVSHOW_ID = 224579

def random_MovieID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_MOVIE_ID)
		response = requests.get(f"https://api.themoviedb.org/3/movie/{random_id}?api_key={THEMOVIEDB_API_KEY}")
		if not hasattr(response.json(), 'status_code'):
			not_valid = False
	return (response.json()['id'])

def random_TVShowID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_TVSHOW_ID)
		response = requests.get(f"https://api.themoviedb.org/3/tv/{random_id}?api_key={THEMOVIEDB_API_KEY}")
		if not hasattr(response.json(), 'status_code'):
			not_valid = False
	return (response.json()['id'])


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