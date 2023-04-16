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
def Movie():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_MOVIE_ID)
		response = requests.get(f"https://api.themoviedb.org/3/movie/{random_id}?api_key={THEMOVIEDB_API_KEY}").json()

		try:
			media_object = {
				"type": 'movie', 
				"name": response['original_title'], 
				"imageURL": f"https://image.tmdb.org/t/p/original{response['poster_path']}"
				}
			if(response['poster_path'] is not None):
				not_valid = False
		except Exception as e: 
			print(e)

	return media_object

# return a ('tv_show', tvshowID)
def TVShow():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_TVSHOW_ID)
		response = requests.get(f"https://api.themoviedb.org/3/tv/{random_id}?api_key={THEMOVIEDB_API_KEY}").json()

		try:
			media_object = {
				"type": 'TV show', 
				"name": response['name'], 
				"imageURL": f"https://image.tmdb.org/t/p/original{response['poster_path']}"
			}
			if(response['poster_path'] is not None):
				not_valid = False
		except Exception as e: 
			print(e)

	return media_object

# return a ('videogame', videogameID)
def Game():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_GAME_ID)
		response = requests.get(f"https://api.rawg.io/api/games/{random_id}?key={RAWG_API_KEY}").json()

		try:
			media_object = {
				"type": 'videogame',  
				"name": response['name'], 
				"imageURL": response['background_image']
			}
			not_valid = False
		except Exception as e: 
			print(e)
	return media_object