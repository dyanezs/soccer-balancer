from src.loader import load_players, load_current_players
from src.display import print_teams_with_ratings, print_teams_for_sharing, print_possible_combinations
from src.balancer import balancer_rating, balancer_brute_force, balancer_karmarkar_karp, balancer_random_trials, balancer_brute_force_all_optimal


def main():

    players = load_current_players("data/player_attendance.csv")
    player_ratings = load_players("data/player_ratings.csv", players)
    
    n = print_possible_combinations(player_ratings)
    
    print('------ Greedy Algorithm ------')
    team_a, team_b = balancer_rating(player_ratings)
    print_teams_with_ratings(team_a, team_b)
    
    print('------ Karmarkar Karp ------')
    team_a, team_b = balancer_karmarkar_karp(player_ratings)
    print_teams_with_ratings(team_a, team_b)
    
    print('------ Random Trials ------')
    team_a, team_b = balancer_random_trials(player_ratings, int(n/2))
    print_teams_with_ratings(team_a, team_b)
    
    print('\n\n------ Brute Force Algorithm ------')
    team_a, team_b = balancer_brute_force(player_ratings)
    print_teams_with_ratings(team_a, team_b)

    print('\n\n------ Brute Force Algorithm - All Combinations------')
    all_optimal_teams = balancer_brute_force_all_optimal(player_ratings)

    for i, (team_a, team_b) in enumerate(all_optimal_teams, 1):
        print(f"\n--- Optimum Combination #{i} ---")
        print_teams_with_ratings(team_a, team_b)

    print_teams_for_sharing(team_a, team_b)


if __name__ == "__main__":
    main()