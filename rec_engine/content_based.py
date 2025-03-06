# Content based filtering

# Import statements
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np

def rec_tfidf_setup(df):
    """Add TFIDF layer to get similarity between books

    Args:
        df (Datframe): Books dataframe

    Returns:
        cosine_sim: Pairwise similarity scores
        indices: Indices corresponding to book titles
    """
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['Description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    return cosine_sim, indices

def semantic_setup(df):
    """Add semantic layer to get similarity between books

    Args:
        df (Datframe): Books dataframe

    Returns:
        cosine_sim: Pairwise similarity scores
        indices: Indices corresponding to book titles
    """
    nlp = spacy.load("en_core_web_md") # need to download separately using python -m spacy download en_core_web_md

    df = df.dropna(subset=['Title', 'Description'])
    df['vector'] = df['Description'].apply(lambda desc: nlp(desc).vector)  # Convert to vectors
    embeddings = np.vstack(df['vector'].values)  # Stack vectors
    cosine_sim = cosine_similarity(embeddings)  # Compute similarity
    indices = pd.Series(df.index, index=df['Title']).drop_duplicates()
    return cosine_sim, indices

def generate_recs(df, title, num_recommend):
    """Generate top n recommendations

    Args:
        df (Dataframe): Books dataframe
        title (str): Title of book for which recommendations are needed
        num_recommend (int): Number of recommendations to be generated

    Returns:
        recs (Dataframe): Recommendations data
    """
    print('Generating recommendations...')
    
    # Combined similarity scores using TFIDF and Semantic Layering
    tfidf_sim, indices = rec_tfidf_setup(df)
    semantic_sim, _ = semantic_setup(df)
    combined_sim = 0.2 * tfidf_sim + (1 - 0.2) * semantic_sim  # weighted combination - can be adjusted
    idx = indices[title]

    # Get the pairwsie similarity scores of all books with given book
    sim_scores = list(enumerate(combined_sim[idx]))
    
    # Sort the movies based on the similarity scores to get top books
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_similar = sim_scores[1:num_recommend+1]
    
    # Return the top most similar movies
    book_indices = [i[0] for i in top_similar]
    
    return df['Title'].iloc[book_indices]

    
