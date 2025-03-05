# Content based filtering

# Import statements
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import sys
import os
print(sys.path)

def rec_setup(df):
    # Create a TfidfVectorizer and Remove stopwords
    tfidf = TfidfVectorizer(stop_words='english')
    # Fit and transform the data to a tfidf matrix
    tfidf_matrix = tfidf.fit_transform(df['Description'])
    # Compute the cosine similarity between each movie description
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    return cosine_sim, indices

def generate_recs(df, title, num_recommend):
    cosine_sim, indices = rec_setup(df)

    idx = indices[title]
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    top_similar = sim_scores[1:num_recommend+1]
    # Get the movie indices
    movie_indices = [i[0] for i in top_similar]
    # Return the top 10 most similar movies
    return df[title].iloc[movie_indices]

    
