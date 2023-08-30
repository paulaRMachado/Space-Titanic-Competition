import pandas as pd

def get_data(path):
    df = pd.read_csv(path)
    return df

def save_csv(path, df):
    df.to_csv(path)
    return