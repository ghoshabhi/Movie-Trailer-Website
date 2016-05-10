import webbrowser

class Movie():
    """ This is documentation! Following variables represent the respective information :
        1)self : the object itself
        2)movie_title : The title of the movie
        3)movie_storyline : Description about the movie
        4)movie_artist : Names of Artists in the movie.
	5)poster_image : Image of the poster of the movie.
	6)trailer_youtube : URL of the trailer from YouTube.
    """

    def __init__(self,movie_title,movie_storyline,movie_artist,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.artist = movie_artist
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# show_trailer(self) takes a URL and opens it in a web-browser(i-frame)
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
