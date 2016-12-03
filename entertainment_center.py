import media
import fresh_tomatoes

# create nine favorite movie objects
whiplash = media.Movie("Whiplash", "movie about obsession",
                       "https://upload.wikimedia.org/wikipedia/ru/0/01/Whiplash_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=7d_jQycdQGo")

neon_demon = media.Movie("Neon Demon", "movie about external world",
                         "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Neon_Demon.png",  # NOQA
                         "https://www.youtube.com/watch?v=cipOTUO0CmU")

enter_the_void = media.Movie("Enter The Void", "movie about us",
                             "https://upload.wikimedia.org/wikipedia/en/3/39/Enter-the-void-poster.png",  # NOQA
                             "https://www.youtube.com/watch?v=bKRxDP--e-Y")

swiss_army_man = media.Movie("Swiss Army Man", "movie about hidden loneliness",
                             "https://upload.wikimedia.org/wikipedia/en/7/72/Swiss_Army_Man_poster.png",  # NOQA
                             "https://www.youtube.com/watch?v=yrK1f4TsQfM")

melancholia = media.Movie("Melancholia", "movie about inner state",
                          "https://upload.wikimedia.org/wikipedia/en/e/e1/Melancholia_Poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=wzD0U841LRM")

two_days_one_night = media.Movie("Two Days, One Night", "movie about fear",
                                 "https://upload.wikimedia.org/wikipedia/en/3/3d/Deux_jours%2C_une_nuit_poster.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=Tb3zBq6gVRk")

yes_and_yes = media.Movie("Yes and yes", "movie about first love",
                          "https://upload.wikimedia.org/wikipedia/ru/c/c8/%D0%9F%D0%BE%D1%81%D1%82%D0%B5%D1%80_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%D0%B0_%C2%AB%D0%94%D0%B0_%D0%B8_%D0%94%D0%B0%C2%BB.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=t8KE_IqKXus")

knight_of_cups = media.Movie("Knight of cups", "movie about finding self",
                             "https://upload.wikimedia.org/wikipedia/en/c/c4/Knight_of_Cups_poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=SI2j1FHCjtM")

mulholland_drive = media.Movie("Mulholland Drive",
                               "movie about hopes and desires",
                               "https://upload.wikimedia.org/wikipedia/en/0/0f/Mulholland.png",  # NOQA
                               "https://www.youtube.com/watch?v=VHPKe8D01Kk")

# create list with favorite movies
movies = [enter_the_void, whiplash, neon_demon,
          swiss_army_man, two_days_one_night, melancholia,
          yes_and_yes, knight_of_cups, mulholland_drive]

# open website in browser
fresh_tomatoes.open_movies_page(movies)
