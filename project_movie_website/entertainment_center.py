import fresh_tomatoes
import media

bottle_rocket = media.Movie("Bottle Rocket",
                            "I have never heard a synopsis that does this movie justice.\n"
                            "The plot isn't the point, it is the feeling and the characters that bring it life.",
                            "https://upload.wikimedia.org/wikipedia/en/a/ae/Bottle-Rocket.jpg",
                            "https://www.youtube.com/watch?v=RY3iBfth1Ro")

meet_joe_black = media.Movie("Meet Joe Black",
                             "Death takes a vacation and falls in love.",
                             "https://upload.wikimedia.org/wikipedia/en/f/f5/Meet_Joe_Black-_1998.jpg",
                             "https://www.youtube.com/watch?v=_zIOjl93WrU")

movies = [bottle_rocket, meet_joe_black]
fresh_tomatoes.open_movies_page(movies)

