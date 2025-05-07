import pandas as pd

def load_roommate_data(file_path):
    return pd.read_csv(file_path)

def get_roommate_profiles(df):
    return df.to_dict(orient='records')
