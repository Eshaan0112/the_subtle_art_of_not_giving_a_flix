# Import statements
import pandas as pd
from data_collection.read_data import main_data_collection
from EDA.explore import preprocess
from content_based import generate_recs

if __name__=="__main__":
    # Get dataset - run only once
    # main_data_collection()

    # Preprocess dataset
    df = pd.read_csv("books_dataset.csv")
    df = preprocess(df)

    # Generate recommendations
    book, num = 'Radiance', 10 # num set of books that are able to be recommended:  df['Title'].to_list()
    recs = generate_recs(df,book, num) # top num recommendations
    print(f'Top {num} recommendations:')
    print(recs)
    