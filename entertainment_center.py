#!/usr/bin/env python

import media
import fresh_tomatoes

def builtin_movies():
    # Our list of movies. The movies are just ones that I enjoy. ;)
    movies = [
        media.Movie("Oscar",
                    "https://www.youtube.com/watch?v=CMMtpC7t4s4",
                    "https://upload.wikimedia.org/wikipedia/en/3/31/Oscar1991poster.jpg"),
        media.Movie("The R.M.",
                    "https://www.youtube.com/watch?v=qGTkCLhM12o",
                    "https://upload.wikimedia.org/wikipedia/en/3/3c/The_R.M._poster.jpg"),
        media.Movie("Napoleon Dynamite",
                    "https://www.youtube.com/watch?v=ZHDi_AnqwN4",
                    "https://upload.wikimedia.org/wikipedia/en/8/87/Napoleon_dynamite_post.jpg"),
        media.Movie("The Lord of the Rings",
                    "https://www.youtube.com/watch?v=V75dMMIW2B4",
                    "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg"),
    ]
    return movies

import tmdbsimple as tmdb
import os

tmdb.API_KEY = os.environ.get('TMDB_API_KEY')
TMDB_IMAGE_URL_BASE = "https://image.tmdb.org/t/p/original"

def tmdb_movies():
    discover = tmdb.Discover()
    response = discover.movie(page=1, year=2017)
    def tmdb_to_movie(tmdb_movie):
        return media.Movie(tmdb_movie['title'], "https://www.youtube.com/watch?v=dQw4w9WgXcQ", TMDB_IMAGE_URL_BASE + tmdb_movie['poster_path'])

    tmdb_movies = list(map(tmdb_to_movie, discover.results))
    return tmdb_movies

movies = []
if tmdb.API_KEY == None:
    print("TMDB_API_KEY was none, using internal list")
    movies = builtin_movies()
else:
    print("Getting data from TMDB")
    movies = tmdb_movies()

# Show the page in a browser
fresh_tomatoes.open_movies_page(movies)
