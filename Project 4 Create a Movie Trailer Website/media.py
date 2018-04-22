# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser
import sys

class Movie():
    """This class provides a way to store movie related information"""
    valid_ratings = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_production, movie_release_year,  movie_storyline, poster_image_url,trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.production = movie_production
        self.release_year = movie_release_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Adding condition to check for system platform and call Safari directly in OSX"""
        if sys.platform == 'darwin':
            browser=webbrowser.get("Safari")
            browser.open(self.trailer_youtube_url)
        else:
            webbrowser.open(self.trailer_youtube_url)
