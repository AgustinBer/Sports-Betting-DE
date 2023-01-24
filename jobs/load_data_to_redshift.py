import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timedelta


def load_data_to_redshift(**kwargs):

    execution_date = kwargs["execution_date"]
    prev_execution_date = execution_date - timedelta(days=1)
    yesterday = prev_execution_date.strftime("%Y-%m-%d")

    # create Redshift connection
    engine = create_engine(
        "redshift+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
            user="", password="", host="", port="", database=""
        )
    )

    # load games dataframe
    games_df = pd.read_csv("data/processed/games_{}.csv".format(yesterday))
    games_df.to_sql("games", engine, if_exists="append", index=False)

    # load scores dataframe
    scores_df = pd.read_csv("data/processed/scores_{}.csv".format(yesterday))
    scores_df.to_sql("scores", engine, if_exists="append", index=False)

    # load status dataframe
    status_df = pd.read_csv("data/processed/status_{}.csv".format(yesterday))
    status_df.to_sql("status", engine, if_exists="append", index=False)

    # load teams dataframe
    teams_df = pd.read_csv("data/processed/teams_{}.csv".format(yesterday))
    teams_df.to_sql("teams", engine, if_exists="append", index=False)

    # load leagues dataframe
    leagues_df = pd.read_csv("data/processed/leagues_{}.csv".format(yesterday))
    leagues_df.to_sql("leagues", engine, if_exists="append", index=False)

    # load countries dataframe
    countries_df = pd.read_csv("data/processed/countries_{}.csv".format(yesterday))
    countries_df.to_sql("countries", engine, if_exists="append", index=False)

    # load scores dataframe
    leagues_df = pd.read_csv("data/processed/scores_{}.csv".format(yesterday))
    leagues_df.to_sql("scores", engine, if_exists="append", index=False)
