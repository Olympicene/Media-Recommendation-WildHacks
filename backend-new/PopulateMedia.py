import RandomMedia as random
import db
from pathlib import Path

DB_FILE = "media.db"

# create db file if not exist
filePath = Path(DB_FILE)
filePath.touch(exist_ok= True)

# connect and create media table
dbconn = db.create_connection(DB_FILE)
db.create_media_table(dbconn)

db.add_media(dbconn, random.Movie())
db.add_media(dbconn, random.TVShow())
db.add_media(dbconn, random.Game())
