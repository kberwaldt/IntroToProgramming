# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

requiem_for_a_dream = media.Movie("Requiem for a Dream","Thousand Words & Protozoa Pictures","2001","A film depicting different forms of drug addiction","https://upload.wikimedia.org/wikipedia/en/9/92/Requiem_for_a_dream.jpg","https://www.youtube.com/watch?v=0nU7dC9bIDg")

#print(toy_story.storyline)

rocky = media.Movie("Rocky","Chartoff-Winkler Productions","2001","Small time club fight that gets a shot at the world heavyweight championship","https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg","https://www.youtube.com/watch?v=3VUblDwa648")

faf = media.Movie("Fast and Furious","Universal Pictures","2001","Illegal street racing and heists","http://vignette1.wikia.nocookie.net/fastandfurious/images/0/04/The_Fast_and_the_Furious_%28DVD_Cover%29.jpeg/revision/latest?cb=20150501043627","https://www.youtube.com/watch?v=ZsJz2TJAPjw")

#print(faf.storyline)
#avatar.show_trailer()
#faf.show_trailer()

movies = [requiem_for_a_dream, rocky, faf]
fresh_tomatoes.open_movies_page(movies)
