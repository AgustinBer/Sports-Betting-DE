import json
from datetime import datetime, timedelta
import pandas as pd

# calculate the date for the previous day


def data_cleaning(**kwargs):
    execution_date = kwargs['execution_date']
    prev_execution_date = execution_date - timedelta(days=1)
    yesterday = prev_execution_date.strftime("%Y-%m-%d")
    
    # load the data from the file
    with open("data/raw/basketball_games_{}.json".format(yesterday), "r") as f:
        data = json.load(f)
    games_df = pd.json_normalize(data['response'], sep='_')
    games_df = games_df.rename(columns={'teams_home_id': 'home_team_id', 
                                        'teams_away_id': 'away_team_id', 
                                        'teams_home_name': 'home_team_name', 
                                        'teams_away_name': 'away_team_name', 
                                        'scores_home_total': 
                                        'home_team_total_score', 
                                        'scores_away_total': 
                                        'away_team_total_score'})

    teams_df = games_df[['home_team_id', 'home_team_name', 'away_team_id', 'away_team_name']]
    teams_df = teams_df.drop_duplicates()
    teams_df.to_csv("data/processed/teams_{}.csv".format(yesterday), index=False)

    scores_df = games_df[['home_team_quarter_1', 'home_team_quarter_2', 'home_team_quarter_3', 
                          'home_team_quarter_4', 'home_team_over_time', 'home_team_total_score', 
                          'away_team_quarter_1', 'away_team_quarter_2', 'away_team_quarter_3', 'away_team_quarter_4', 
                          'away_team_over_time', 'away_team_total_score']]
    
    scores_df.to_csv("data/processed/scores_{}.csv".format(yesterday), index=False)

    league_df = games_df[['league_id', 'league_name', 'league_type', 'league_season', 'league_logo']]
    league_df = league_df.drop_duplicates()
    # league_df.to_csv("data
