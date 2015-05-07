import webbrowser  # required to open up the browser


class Movie():
    """This class stores the values for the movies displayed on the page"""
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, imdb, year_released):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.IMDb_rating = imdb        # Some more information to be rendered
        self.release_year = year_released

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
