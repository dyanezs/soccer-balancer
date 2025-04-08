def print_teams_with_ratings(df_a, df_b):
    """
    Muestra los equipos con los ratings para no compartir, usando DataFrames.
    """
    def print_team_with_ratings(name, df):
        total_rating = df["rating"].sum()
        print(f"\n{name} (Total Rating: {total_rating}):")
        for _, row in df.iterrows():
            print(f"  {row['name']} {row['last_name']} - Rating: {row['rating']}")
    
    print_team_with_ratings("Equipo Naranja", df_a)
    print_team_with_ratings("Equipo Azul", df_b)


def print_teams_for_sharing(df_a, df_b):
    """
    Muestra los equipos sin los ratings, pero con las probabilidades de victoria.
    """
    def calculate_probability(df_a, df_b):
        """
        Calcula las probabilidades de victoria considerando ratings.
        """
        rating_a = df_a["rating"].sum()
        rating_b = df_b["rating"].sum()
        
        # Calcular probabilidad de empate basada en la diferencia de ratings
        diff_rating = abs(rating_a - rating_b)
        prob_empate = max(0, min(0.5, (1 - (diff_rating / (rating_a + rating_b)))) )
        
        prob_a = (rating_a / (rating_a + rating_b - prob_empate)) * (1 - prob_empate)
        prob_b = (rating_b / (rating_a + rating_b - prob_empate)) * (1 - prob_empate)
        
        return prob_empate, prob_a, prob_b

    # Calcular las probabilidades
    prob_empate, prob_a, prob_b = calculate_probability(df_a, df_b)

    def print_team_for_sharing(name, df, prob):
        """
        Imprime los jugadores sin ratings y con probabilidades, desordenados.
        """
        shuffled_df = df.sample(frac=1).reset_index(drop=True)  # Desordenar DataFrame
        print(f"\n{name} (Probabilidad de victoria: {prob:.0%}):")
        for _, row in shuffled_df.iterrows():
            print(f"  {row['name']} {row['last_name']}")
    
    print_team_for_sharing("Equipo Naranja", df_a, prob_a)
    print_team_for_sharing("Equipo Azul", df_b, prob_b)
    print(f"\nProbabilidad de empate: {prob_empate:.0%}")
