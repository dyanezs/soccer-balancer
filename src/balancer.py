import pandas as pd
from itertools import combinations
import random

def balancer_rating(players_df):

    sorted_df = players_df.sort_values(by='rating', ascending=False).copy()

    team_1_rows = []
    team_2_rows = []
    sum_1 = sum_2 = 0

    for _, row in sorted_df.iterrows():
        if sum_1 <= sum_2:
            team_1_rows.append(row)
            sum_1 += row["rating"]
        else:
            team_2_rows.append(row)
            sum_2 += row["rating"]

    team_1_df = pd.DataFrame(team_1_rows)
    team_2_df = pd.DataFrame(team_2_rows)

    return team_1_df, team_2_df


# --------------------
# 1. Fuerza Bruta (Exhaustive Search)
# --------------------
def balancer_brute_force(players_df):
    n = len(players_df)
    if n % 2 != 0:
        raise ValueError("Número impar de jugadores, no se puede dividir equitativamente.")

    min_diff = float("inf")
    best_team_a, best_team_b = None, None
    indices = list(range(n))
    player_list = players_df.reset_index(drop=True)

    for combo in combinations(indices, n // 2):
        team_a = player_list.loc[list(combo)]
        team_b = player_list.drop(index=list(combo))

        diff = abs(team_a["rating"].sum() - team_b["rating"].sum())
        if diff < min_diff:
            min_diff = diff
            best_team_a = team_a
            best_team_b = team_b

    return best_team_a, best_team_b


def balancer_brute_force_all_optimal(players_df):
    players = players_df.to_dict("records")
    n = len(players)

    if n % 2 != 0:
        raise ValueError("Número de jugadores debe ser par para el balanceo exacto.")

    min_diff = float('inf')
    best_combinations = []

    indices = list(range(n))
    half_n = n // 2

    for combo_indices in combinations(indices, half_n):
        team1 = [players[i] for i in combo_indices]
        team2 = [players[i] for i in indices if i not in combo_indices]

        rating1 = sum(p["rating"] for p in team1)
        rating2 = sum(p["rating"] for p in team2)

        diff = abs(rating1 - rating2)

        if diff < min_diff:
            min_diff = diff
            best_combinations = [(team1, team2)]
        elif diff == min_diff:
            best_combinations.append((team1, team2))

    # Mostrar cantidad de combinaciones óptimas
    print(f"Se encontraron {len(best_combinations)} combinaciones óptimas con diferencia mínima de rating: {min_diff}")

    results = []
    for team1, team2 in best_combinations:
        df1 = pd.DataFrame(team1)
        df2 = pd.DataFrame(team2)
        results.append((df1, df2))

    return results

# --------------------
# 2. Karmarkar-Karp Heurística
# --------------------
def balancer_karmarkar_karp(players_df):
    player_list = players_df.sort_values("rating", ascending=False).reset_index(drop=True)
    team_1 = pd.DataFrame(columns=players_df.columns)
    team_2 = pd.DataFrame(columns=players_df.columns)
    sum_1 = sum_2 = 0

    for _, row in player_list.iterrows():
        if sum_1 <= sum_2:
            team_1 = pd.concat([team_1, row.to_frame().T], ignore_index=True)
            sum_1 += row["rating"]
        else:
            team_2 = pd.concat([team_2, row.to_frame().T], ignore_index=True)
            sum_2 += row["rating"]

    return team_1, team_2


# --------------------
# 3. Random con múltiples intentos
# --------------------
def balancer_random_trials(players_df, n_trials=10000):
    n = len(players_df)
    if n % 2 != 0:
        raise ValueError("Número impar de jugadores, no se puede dividir equitativamente.")

    best_team_a, best_team_b = None, None
    min_diff = float("inf")

    for _ in range(n_trials):
        shuffled = players_df.sample(frac=1).reset_index(drop=True)
        team_a = shuffled.iloc[:n // 2]
        team_b = shuffled.iloc[n // 2:]

        diff = abs(team_a["rating"].sum() - team_b["rating"].sum())
        if diff < min_diff:
            min_diff = diff
            best_team_a = team_a
            best_team_b = team_b

    return best_team_a, best_team_b
