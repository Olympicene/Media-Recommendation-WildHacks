import requests
import os
import random
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
THEMOVIEDB_API_KEY = os.getenv('THEMOVIEDB_API_KEY')
RAWG_API_KEY = os.getenv('RAWG_API_KEY')

# UGLY CONTSTANTS
MAX_MOVIE_ID = 1113623
MAX_TVSHOW_ID = 224579
MAX_GAME_ID = 58134

# return a ('movie', movieID)
def random_MovieID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_MOVIE_ID)
		response = requests.get(f"https://api.themoviedb.org/3/movie/{random_id}?api_key={THEMOVIEDB_API_KEY}").json()

		try:
			media_object = {
				"type": 'movie', 
				"id": response['id'], 
				"name": response['original_title'], 
				"image_url": f"https://image.tmdb.org/t/p/original{response['poster_path']}"
				}
			not_valid = False
		except Exception as e: 
			print(e)

	return media_object

# return a ('tv_show', tvshowID)
def random_TVShowID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_TVSHOW_ID)
		response = requests.get(f"https://api.themoviedb.org/3/tv/{random_id}?api_key={THEMOVIEDB_API_KEY}").json()

		try:
			media_object = {
				"type": 'tv_show', 
				"id": response['id'], 
				"name": response['name'], 
				"image_url": f"https://image.tmdb.org/t/p/original{response['poster_path']}"
			}
			not_valid = False
		except Exception as e: 
			print(e)

	return media_object

# return a ('videogame', videogameID)
def random_GamesID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_GAME_ID)
		response = requests.get(f"https://api.rawg.io/api/games/{random_id}?key={RAWG_API_KEY}").json()

		try:
			media_object = {
				"type": 'videogame',  
				"id": response['id'], 
				"name": response['name'], 
				"image_url": response['background_image']
			}
			not_valid = False
		except Exception as e: 
			print(e)

	return media_object

print(random_GamesID())
