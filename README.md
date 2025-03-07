# Content Based Filtering Recommendation System for Google Books

## Foundational concepts
Content Based Filtering: This short tutorial should help you with the basics of recommendation systems: [rec_system](https://www.geeksforgeeks.org/ml-content-based-recommender-system/)

   
## Data details
Please refer to `data_collection/read_data.py` for details on using Google API books dataset using
[this](https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&startIndex={start_index})

## What the project does
1. Project statement: 
This recommendation system provides user specified 'n' book recommendations across multiple genres using a Content Based Filtering system. You can refer to this design for a high level walkthrough:
![High Level Design](HLD.png)
2. Tokenization and semantic layering of words:
Tokenization and semantic layering of words in descriptions of books is used to calculate cosine similarity as a weighted sum to rank top 'n' books.
3. Embeddings for semantic layering:
Word vectors are dense numerical representations of words. Words with similar meanings have similar vector representations, capturing their semantic similarity. I use pre-trained word vectors from `spacy` (en_core_web_md) that are trained on large corpora, like Wikipedia, to represent words in a multi-dimensional space.

## How to run the project
After setting up the poetry environment: 
Run recommendation system from: `/the_subtle_art_of_giving_a_flix/rec_engine` as `python end2end.py`
  



