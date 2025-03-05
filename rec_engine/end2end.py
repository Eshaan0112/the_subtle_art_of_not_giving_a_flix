# Import statements

import pandas as pd
from data_collection.read_data import main_data_collection
from EDA.explore import preprocess
from content_based import generate_recs

if __name__=="__main__":
    # Get dataset
    main_data_collection()

    # Preprocess dataset
    df = pd.read_csv("books_dataset.csv")
    df = preprocess(df)

    print(sys.path)
    # Generate recommendations
    recs = generate_recs(df, 'The Fault in Our Stars', 2)
    print(recs)
    