import pandas as pd
from src.balancer import balancer_rating

def test_balancer_balances_well():
    data = {
        "id": [1, 2, 3, 4],
        "name": ["A", "B", "C", "D"],
        "last_name": ["", "", "", ""],
        "rating": [10, 9, 6, 5]
    }
    df = pd.DataFrame(data)
    team_a, team_b = balancer_rating(df)
    
    total_a = team_a["rating"].sum()
    total_b = team_b["rating"].sum()
    assert abs(total_a - total_b) <= 2
