import csv
import pandas as pd
import random


def load_players(file_path, current_players):
    """Loads player ratings"""

    ratings_df = pd.read_csv(file_path)
    current_ids = current_players['id'].unique()
    current_players_df = ratings_df[ratings_df['id'].isin(current_ids)].copy()

    return current_players_df


def load_current_players(file_path, match_date=None):
    """Loads player attendance"""

    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])

    if match_date is None:
        latest_date = df['date'].max()
        print(f"Using last date available: {latest_date.date()}")
        return df[df['date'] == latest_date]
    else:
        match_date = pd.to_datetime(match_date)
        if match_date not in df['date'].values:
            print(f"No data for this date: {match_date.date()}")
            return pd.DataFrame()
        return df[df['date'] == match_date]

