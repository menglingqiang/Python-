import webbrowser
class Movie:
    '''just test'''
    def __init__(self,movie_title,movie_storyline,poster_imge,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_imge
        self.trailer_youtube_url = trailer_youtube
    def play_movie(self):
        webbrowser.open_new(self.trailer_youtube_url)
        