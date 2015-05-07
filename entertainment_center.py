import fresh_tomatoes  # required to format the HTML page
import media           # imports the document containing the class Movie

# Information and pictures gathered from IMDb

movie1 = media.Movie('The Shawshank Redemption',
                     'Two imprisoned men bond over a number of years, ' +
                     'finding solace and eventual redemption through acts ' +
                     'of common decency.',
                     'http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5B' +
                     'Ml5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.' +
                     'jpgE@._V1_SX214_AL_.jpg',
                     'https://www.youtube.com/watch?v=6hB3S9bIaco',
                     '9.2',
                     '1994')
movie2 = media.Movie('The Godfather',
                     'The aging patriarch of an organized crime dynasty ' +
                     'transfers control of his clandestine empire to his ' +
                     'reluctant son.',
                     'http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5B' +
                     'Ml5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg',
                     'https://www.youtube.com/watch?v=sY1S34973zA',
                     '9.2',
                     '1972')
movie3 = media.Movie('The Godfather: Part II',
                     'The early life and career of Vito Corleone in 1920s ' +
                     'New York is portrayed while his son, Michael, expands ' +
                     'and tightens his grip on his crime syndicate ' +
                     'stretching from Lake Tahoe, Nevada to pre-revolution ' +
                     '1958 Cuba.',
                     'http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl5B' +
                     'Ml5BanBnXkFtZTcwMTA5Mzg3OA@@._V1_SX214_AL_.jpg',
                     'https://www.youtube.com/watch?v=qJr92K_hKl0',
                     '9.1',
                     '1974')

movie4 = media.Movie('The Dark Knight',
                     'When the menace known as the Joker wreaks havoc and ' +
                     'chaos on the people of Gotham, the caped crusader must' +
                     ' come to terms with one of the greatest psychological ' +
                     'tests of his ability to fight injustice.',
                     'http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5B' +
                     'Ml5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,' +
                     '214,317_AL_.jpg',
                     'https://www.youtube.com/watch?v=EXeTwQWrcwY',
                     '9.0',
                     '2008')
movie5 = media.Movie('Pulp Fiction',
                     'The lives of two mob hit men, a boxer, a gangsters' +
                     'wife, and a pair of diner bandits intertwine in four ' +
                     'tales of violence and redemption.',
                     'http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5B' +
                     'Ml5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,' +
                     '214,317_AL_.jpg',
                     'https://www.youtube.com/watch?v=wZBfmBvvotE',
                     '8.9',
                     '1994')
movie6 = media.Movie("Schindler's List",
                     'In Poland during World War II, Oskar Schindler ' +
                     'gradually becomes concerned for his Jewish workforce ' +
                     'after witnessing their persecution by the Nazis.',
                     'http://ia.media-imdb.com/images/M/MV5BMzMwMTM4MDU2N15B' +
                     'Ml5BanBnXkFtZTgwMzQ0MjMxMDE@._V1_SX214_AL_.jpg',
                     'https://www.youtube.com/watch?v=dwfIf1WMhgc',
                     '8.9',
                     '1993')
movies = [movie1, movie2, movie3, movie4, movie5, movie6]  # list of the movies
fresh_tomatoes.open_movies_page(movies)
# runs the list through the fresh tomatoes doc
