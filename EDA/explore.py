import pandas as pd
## TO BE IMPLEMENTED - ONLY INITIALIZED


def preprocess(df):
    df = df.dropna(subset=['Description']) 
    return df


    
