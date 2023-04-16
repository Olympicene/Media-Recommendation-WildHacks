from fastapi import FastAPI
from pydantic import BaseModel
import RandomMedia as random
import db
from pathlib import Path
import time 


DB_FILE = "media.db"

# create db file if not exist
filePath = Path(DB_FILE)
filePath.touch(exist_ok= True)

# connect and create media table
dbconn = db.create_connection(DB_FILE)
db.create_media_table(dbconn)
db.create_pair_table(dbconn)


app = FastAPI()

### REQ REQUESTS

# /rand - get any random row
@app.get("/rand")
def random_pair():
    return db.random_media(dbconn)

# /rows/?id=5 - get specific row
@app.get("/rows/")
async def read_item(id: int = 0):
    return db.get_row(dbconn, id)

### POST REQUESTS

class Item(BaseModel):
    rowID1: int
    rowID2: int

@app.post("/downvote/")
async def down(item: Item):
    pair = {
        "rowID1": item.rowID1,
        "rowID2": item.rowID2,
        "timestamp": time.time(),
        "score": -1,
        "totalVotes": 1
    }

    if(db.pair_exists(dbconn, pair)):
        db.downvote(dbconn, pair);
        return "Downvoted Pairs"
    else:
        db.add_pair(dbconn, pair)
        return "Added new pair to Pairs"

@app.post("/upvote/")
async def up(item: Item):
    pair = {
        "rowID1": item.rowID1,
        "rowID2": item.rowID2,
        "timestamp": time.time(),
        "score": 1,
        "totalVotes": 1
    }

    if(db.pair_exists(dbconn, pair)):
        db.upvote(dbconn, pair);
        return "Upvoted Pairs"
    else:
        db.add_pair(dbconn, pair)
        return "Added new pair to Pairs"