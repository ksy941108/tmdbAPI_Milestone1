import os 
import random
import flask
from tmdb import movie_info
from wikipedia import getURL

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', methods = ["GET", "POST"])

def index():
    MOVIE_IDS = [
        634649, #spiderman no way home
        141, #Donnie Darko
        438631, #Dune
    ]

    random_id = random.choice(MOVIE_IDS) 

    title, tagline, genre, posterImg = movie_info(random_id)

    url = getURL(title)
    
    return flask.render_template ( 
        "index.html", 
        title = title,
        tagline = tagline,
        genre = genre, 
        posterImg = posterImg,
        url = url
        )

app.run (
    host = os.getenv("IP", "0.0.0.0"),
    port = int(os.getenv("PORT", 8080)),
    debug = True
)