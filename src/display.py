import pandas as pd
import math

def print_possible_combinations(players_df):
    """
    Shows the number of possible combinations
    """
    
    n = len(players_df)
    if n % 2 != 0:
        print(f"\n⚠️ Can't be divided in teams with same players: {n} players.")
        return
    total_combinations = math.comb(n, n // 2) // 2
    print(f"\n🔢 Total possible combinations: {total_combinations:,}")
    
    return total_combinations


def print_teams_with_ratings(df_a, df_b):
    """
    Shows teams with ratings. This is not a version to share.
    """
    
    def print_team_with_ratings(name, df):
        total_rating = df["rating"].sum()
        print(f"\n{name} (Total Rating: {total_rating}):")
        for _, row in df.iterrows():
            second_label = row['last_name'] if not pd.isna(row['last_name']) else f"({row['nickname']})"
            print(f"  {row['name']} {second_label} - Rating: {row['rating']}")
    
    print_team_with_ratings("Orange Team", df_a)
    print_team_with_ratings("Blue Team", df_b)


def print_teams_for_sharing(df_a, df_b):
    """
    Shows teams without rating, but with win probabilities
    """
    def calculate_probability(df_a, df_b):
        """
        Calculates win probabilities
        """
        rating_a = df_a["rating"].sum()
        rating_b = df_b["rating"].sum()
        
        # Calculates probabilities of a draw game
        diff_rating = abs(rating_a - rating_b)
        prob_draw = max(0, min(0.5, (1 - (diff_rating / (rating_a + rating_b)))) )
        
        prob_a = (rating_a / (rating_a + rating_b - prob_draw)) * (1 - prob_draw)
        prob_b = 1 - prob_a - prob_draw
        # prob_b = (rating_b / (rating_a + rating_b - prob_draw)) * (1 - prob_draw)
        
        return prob_draw, prob_a, prob_b

    # Calculates probabilities
    prob_draw, prob_a, prob_b = calculate_probability(df_a, df_b)

    def print_team_for_sharing(name, df, prob):
        """
        Prints teams without ratings, with probabilities, shuffled
        """
        shuffled_df = df.sample(frac=1).reset_index(drop=True)  # Shuffles DataFrame
        print(f"\n{name} (Win Probabilities: {prob:.0%}):")
        for _, row in shuffled_df.iterrows():
            second_label = row['last_name'] if not pd.isna(row['last_name']) else f"({row['nickname']})"
            print(f"  {row['name']} {second_label}")
    
    print_team_for_sharing("Orange Team", df_a, prob_a)
    print_team_for_sharing("Blue Team", df_b, prob_b)
    print(f"\nDraw Game Probability: {prob_draw:.0%}")
