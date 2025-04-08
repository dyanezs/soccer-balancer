from src.loader import load_players, load_current_players
from src.display import print_teams_with_ratings, print_teams_for_sharing
from src.balancer import balancer_rating, balancer_brute_force, balancer_karmarkar_karp, balancer_random_trials, balancer_brute_force_all_optimal


if __name__ == "__main__":

    players = load_current_players("data/player_attendance.csv")
    player_ratings = load_players("data/player_ratings.csv", players)

    # team_a, team_b = balancer_brute_force_all_optimal(player_ratings)
    
    all_optimal_teams = balancer_brute_force_all_optimal(player_ratings)

    for i, (team_a, team_b) in enumerate(all_optimal_teams, 1):
        print(f"\n--- Combinación óptima #{i} ---")
        print_teams_with_ratings(team_a, team_b)
    

    print_teams_with_ratings(team_a, team_b)
    print_teams_for_sharing(team_a, team_b)

