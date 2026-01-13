This is a website which gives 5 similar movies related to the movie entered by the user.
The whole idea is to reduce the time the user spent to search similar movies related to what they have already watched.
It uses tmdb database for accessing movie data, their names and their posters.
The model uses CountVectorizer to genrate vectors from text which can work as a tag.
The model uses Cosine Similarity to determine how much a movie is similar to other.