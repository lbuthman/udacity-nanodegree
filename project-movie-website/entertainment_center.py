import fresh_tomatoes
import media
import cli_ui
import tmdbsimple as tmdb

tmdb.API_KEY = "6b3be69c94536097c86c359ff38a0552"
base_poster_url = "https://image.tmdb.org/t/p/w500"
base_trailer_url = "https://www.youtube.com/watch?v="
movies = []


def find_movie(name):
    search = tmdb.Search()
    response = search.movie(query=name)
    return response['results'][0]

""" Returns found movie data, see tmbd api for more information
Searches api based on string movie name
"""


def get_movie_trailer(id):
    movie_details = tmdb.Movies(id)
    response = movie_details.videos()
    return base_trailer_url + response['results'][0]['key']

""" Returns complete URL for movie trailer
Searches api based on numeric id
"""


def add_movie_to_movies(title, info, poster_url, trailer_url):
    movies.append(media.Movie(title, info, poster_url, trailer_url))

"""add selected movie to array"""

# init command line welcome screen
cli_ui.print_welcome_screen()
input_number = 1

while True:

    movie_name = cli_ui.get_movie(input_number)
    if movie_name == 'q' or movie_name == 'quit':
        break

    found_movie = find_movie(movie_name)
    movie_id = found_movie['id']
    movie_title = found_movie['title']
    movie_info = found_movie['overview']
    movie_poster = base_poster_url + found_movie['poster_path']

    # to get movie trailer, you must search by specific movie id
    movie_trailer = get_movie_trailer(movie_id)

    add_movie_to_movies(movie_title, movie_info, movie_poster, movie_trailer)

    input_number += 1
    cli_ui.print_success_message()

fresh_tomatoes.open_movies_page(movies)
cli_ui.print_exit_message()
