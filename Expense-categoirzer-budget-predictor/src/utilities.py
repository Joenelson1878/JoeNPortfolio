import pandas as pd 

def load_transac(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["date"])
    df = df.dropna(subset=["description", "amount"])
    df["category"] = df["category"].str.strip().str.title()
    return df
