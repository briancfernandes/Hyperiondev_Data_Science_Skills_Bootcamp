import spacy
nlp = spacy.load("en_core_web_md")

# Create a function to return which movie a user would watch next if 
# they watched 'Planet Hulk' with the description and location of the
# input file as arguments.


def find_most_similar_movie(watched_description, movie_database_file):
 
    # Preprocess description of the film watched.
    nlp_watched_movie = nlp(watched_description)

    # Initialize variables to store the most similar movie.
    max_similarity = 0
    most_similar_movie = None

    # Read movie database file and calculate similarity for each movie
    # to then return the movie with the most similarity.
    with open(movie_database_file, 'r') as file:
        for line in file:
            title, description = line.strip().split(' :')
            movie_tokens = nlp(description)
            similarity = nlp_watched_movie.similarity(movie_tokens)
            if similarity > max_similarity:
                max_similarity = similarity
                recommended_movie = title

    return recommended_movie


# Applying the inputs for "Planet Hulk".
watched_description = """Will he save their world or destroy it? When 
        the Hulk becomes too dangerous for the Earth, the Illuminati 
        trick Hulk into a shuttle and launch him into space to a planet 
        where the Hulk can live in peace. Unfortunately, Hulk lands on 
        the planet Sakaar where he is sold into slavery and trained as a 
        gladiator.
        """

movie_database_file = "movies.txt"
next_movie = find_most_similar_movie(watched_description, movie_database_file)

# Inform the viewer what the recommended title is to watch next.
print(f"""Based on the viewing of 'Planet Hulk', you might also enjoy 
      '{next_movie}'.""")

