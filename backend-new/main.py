import requests
import os
import random
from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import database
import sqlite3

load_dotenv()
THEMOVIEDB_API_KEY = os.getenv('THEMOVIEDB_API_KEY')
RAWG_API_KEY = os.getenv('RAWG_API_KEY')

# UGLY CONTSTANTS
MAX_MOVIE_ID = 1113623
MAX_TVSHOW_ID = 224579
MAX_GAME_ID = 58134

class Item(BaseModel):
    id1: int
    type1: str
    id2: int
    type2: str

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