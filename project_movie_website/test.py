import tmdbsimple as tmdb

tmdb.API_KEY = "6b3be69c94536097c86c359ff38a0552"

base_poster_url = "https://image.tmdb.org/t/p/w500"
base_trailer_url = "https://www.youtube.com/watch?v="

search = tmdb.Search()
response = search.movie(query="Bottle Rocket")
movie_id = response['results'][0]['id']
print movie_id
print response['results'][0]['overview']
print base_poster_url + response['results'][0]['poster_path']
movie = tmdb.Movies(movie_id)
movie_response = movie.videos()
print movie_response['results'][0]['key']

# movie_details = response['results'][0]
# movie_title = movie_details['title']
# movie_info = movie_details['overview']
# poster_url =

