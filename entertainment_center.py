#!/usr/bin/env python

import media
import fresh_tomatoes

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

# Show the page in a browser
fresh_tomatoes.open_movies_page(movies)
