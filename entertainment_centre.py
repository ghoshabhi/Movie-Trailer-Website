import media
import fresh_tomatoes

# Create instances of class "media"

movie_1 = media.Movie("X-Men Apocalypse",
                      "Some description about it.",
                      "ABC, DEF, GHI",
                      "http://goo.gl/yRBapH",
                      "https://www.youtube.com/watch?v=COvnHv42T-A")

movie_2 = media.Movie("Captain America",
                      "Some description about it.",
                      "ABC, DEF, GHI",
                      "http://goo.gl/B3C5OE",
                      "https://www.youtube.com/watch?v=1L3c17AmCZw")

movie_3 = media.Movie("Batman v/s Superman",
                      "Some description about it!",
                      "ABC, DEF, GHI",
                      "http://goo.gl/lLST2G",
                      "https://www.youtube.com/watch?v=0WWzgGyAH6Y")

movie_4 = media.Movie("Cars 2",
                      "Some description about it!",
                      "ABC, DEF, GHI",
                      "http://goo.gl/FNf2Pp",
                      "https://www.youtube.com/watch?v=lg5hj2c5Nkk")

movie_5 = media.Movie("Perfume",
                      "Some description about it!",
                      "ABC, DEF, GHI",
                      "http://goo.gl/yCP7JI",
                      "https://www.youtube.com/watch?v=zutiIw_2e2g")

movie_6 = media.Movie("The Internship",
                      "Some description about the movie!",
                      "ABC, DEF, GHI",
                      "http://goo.gl/NVFWPN",
                      "https://www.youtube.com/watch?v=cdnoqCViqUo")

# Creating an array of movies
movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

# Invoke the method from fresh_tomatoes.py to create a HTML file
fresh_tomatoes.open_movies_page(movies)
