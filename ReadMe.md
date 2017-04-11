# Movie Trailer Website
This is a project of online movie trailer with its backend coded in Object Oriented Python.

## Files Contained :
1) media.py
	- Class file containing constructor and show_trailer() function which plays a movie trailer.
	- Constructor Parametres are as follows :
	    a)self : indicating the `self` i.e the object itself.
	    b)movie_title : Title of the Movie.
	    c)movie_storyline : Some description about the movie.
	    d)movie_artist : Names of Artists in the movie.
	    e)poster_image : Image of the poster of the movie.
	    f)trailer_youtube : URL of the trailer from YouTube.


2) entertaiment_centre.py :
	- Here instances of the class "media" are created and instantiated with proper values as in the parameter
	- An array is made of the objects that are created of class "media" as the method called from "fresh_tomatoes.py" takes array as parameter

3) fresh_tomatoes.py :
	- A file which gets data from the "entertaiment_centre.py" file and create a HTML file rendering data into it.

## Steps to Run the Project

a) Download the .zip file and unzip into your choice of directory (make sure you have Python installed on your PC)

b) Right click the file "entertainment_centre.py" and select the option which says "Edit with IDLE"

c) Press F5 or go to "Run" in Menu Bar and Select "Run Module" to run the file
