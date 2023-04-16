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
db.create_pair_table(dbconn)


movie = random.Movie()
tvshow = random.TVShow()
game = random.Game()

print("Movie: ", movie)
print("TV Show: ", tvshow)
print("Game: ", game)
approve = input("Do you want to add this media to the media file? (y/n): ")

if approve.lower() == "y":
    db.add_media(dbconn, movie)
    # db.add_media(dbconn, tvshow)
    # db.add_media(dbconn, game)
    print("Media added to media file.")
else:
    print("Media not added to media file.")

