import requests
import os
import random
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
THEMOVIEDB_API_KEY = os.getenv('THEMOVIEDB_API_KEY')
RAWG_API_KEY = os.getenv('RAWG_API_KEY')

# UGLY CONTSTANTS
MAX_MOVIE_ID = 1113623
MAX_TVSHOW_ID = 224579
MAX_GAME_ID = 58134

def random_MovieID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_MOVIE_ID)
		response = requests.get(f"https://api.themoviedb.org/3/movie/{random_id}?api_key={THEMOVIEDB_API_KEY}")
		if not hasattr(response.json(), 'status_code'):
			not_valid = False
	return ('movie', response.json()['id'])

def random_TVShowID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_TVSHOW_ID)
		response = requests.get(f"https://api.themoviedb.org/3/tv/{random_id}?api_key={THEMOVIEDB_API_KEY}")
		if not hasattr(response.json(), 'status_code'):
			not_valid = False
	return ('tv', response.json()['id'])

def random_GamesID():
	not_valid = True
	while not_valid:
		random_id = random.randint(0, MAX_GAME_ID)
		response = requests.get(f"https://api.rawg.io/api/games/{random_id}?key={RAWG_API_KEY}")
		if not hasattr(response.json(), 'detail'):
			not_valid = False
	return (response.json()['id'])

