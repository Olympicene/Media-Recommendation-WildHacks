import requests
import os
from fastapi import FastAPI
from dotenv import load_dotenv

headers = {
	"Authorization": f"Bearer {THEMOVEDB_API_KEY}",
	"Content-Type": "application/json;charset=utf-8",
}

response = requests.get('https://api.themoviedb.org/3/movie/76341', headers=headers)
print(response)