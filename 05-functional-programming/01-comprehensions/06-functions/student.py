def movie_count(movies, director):
    return len([movie.director for movie in movies if director == movie.director])

def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])

def has_director_made_genre(movies, director, genre):
    return any(genre in movie.genres and movie.director == director for movie in movies)


def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2

def is_increasing(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))

def count_matching(xs, ys):
    return len([x for x in zip(xs, ys) if x[0]==x[1]])

def weighted_sum(ns, weight):
    return sum([a*b for a,b in zip(ns, weight)])

def alternating_caps(string):
    chars = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(string)]
    return "".join(chars)

def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}
