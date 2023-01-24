import great_expectations as ge
import pandas as pd

from datetime import datetime, timedelta

yesterday = datetime.now() - timedelta(days=1)
yesterday = yesterday.strftime("%Y-%m-%d")


def data_validation():
    # load the data from the file
    teams_df = pd.read_csv("data/processed/teams_{}.csv".format(yesterday))
    scores_df = pd.read_csv("data/processed/scores_{}.csv".format(yesterday))
    league_df = pd.read_csv("data/processed/league_{}.csv".format(yesterday))
    status_df = pd.read_csv("data/processed/status_{}.csv".format(yesterday))
    country_df = pd.read_csv("data/processed/country_{}.csv".format(yesterday))
    games_df = pd.read_csv("data/processed/games_{}.csv".format(yesterday))

    # Create a Great Expectations dataset
    teams_dataset = ge.dataset.PandasDataset(teams_df)
    scores_dataset = ge.dataset.PandasDataset(scores_df)
    league_dataset = ge.dataset.PandasDataset(league_df)
    status_dataset = ge.dataset.PandasDataset(status_df)
    country_dataset = ge.dataset.PandasDataset(country_df)
    games_dataset = ge.dataset.PandasDataset(games_df)

    # Validate the data
    teams_validation_result = teams_dataset.validate()
    scores_validation_result = scores_dataset.validate()
    league_validation_result = league_dataset.validate()
    status_validation_result = status_dataset.validate()
    country_validation_result = country_dataset.validate()
    games_validation_result = games_dataset.validate()
