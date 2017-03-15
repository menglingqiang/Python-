import movie
import webbrowser
import movie_player
animal = movie.Movie('animal','animals sing songs','https://imgsa.baidu.com/baike/c0%3Dbaike220%2C5%2C5%2C220%2C73/sign=a71afe23fadeb48fef64a98c9176514c/a71ea8d3fd1f4134cdea613c2c1f95cad0c85e96.jpg','https://www.youtube.com/watch?v=ke2sYmDr_JM')
#print(animal.title)
#animal.play_movie()
movies = [animal]
movie_player.open_movies_page(movies)