import requests
import os
import random
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
THEMOVIEDB_API_KEY = os.getenv('THEMOVIEDB_API_KEY')
RAWG_API_KEY = os.getenv('RAWG_API_KEY')

# UGLY CONTSTANTS
MAX_MOVIE_ID = 1113623
MAX_TVSHOW_ID = 224579
MAX_GAME_ID = 58134

# class Item(BaseModel):
#     id1: int
#     type1: str 
#     id2: int
#     type2: str 
class Item(BaseModel):
    id1: int
    type1: str | None = None
    id2: int
    type2: str | None = None
 

# return a ('movie', movieID)
def random_MovieID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_MOVIE_ID)
		response = requests.get(f"https://api.themoviedb.org/3/movie/{random_id}?api_key={THEMOVIEDB_API_KEY}").json()
		print("sending a response", response)
		if 'id' in response:
			not_valid = False
	return ('movie', response['id'])

# return a ('tv_show', tvshowID)
def random_TVShowID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_TVSHOW_ID)
		response = requests.get(f"https://api.themoviedb.org/3/tv/{random_id}?api_key={THEMOVIEDB_API_KEY}").json()
		if 'id' in response:
			not_valid = False
	return ('tv_show', response['id'])

# return a ('videogame', videogameID)
def random_GamesID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_GAME_ID)
		response = requests.get(f"https://api.rawg.io/api/games/{random_id}?key={RAWG_API_KEY}").json()
		if 'detail' not in response:
			not_valid = False
	return ('videogame',  response['id'])

# return a list of 2 multimedia tuples
def random_multimedia_pair():
	multimedia = [random_GamesID, random_MovieID, random_TVShowID]
	obj = random.choice(multimedia)() + random.choice(multimedia)() 
	type1, id1, type2, id2 = obj[0], obj[1], obj[2], obj[3]
	return {
			"id1" : id1,
			"type1" : type1,
			"id2" : id2,
			"type2" : type2,
			"score" : 0,
			"totalvotes" : 0
	}
	
	#return {random.choice(multimedia)(), random.choice(multimedia)(), "this is some bullshit"}

app = FastAPI()

@app.get("/rand")
def random_pair():
    return random_multimedia_pair()

@app.post("/downvote/")
async def down(item: Item):
    return item

@app.post("/upvote/")
async def up(item: Item):
    return item

# print(random_MovieID())