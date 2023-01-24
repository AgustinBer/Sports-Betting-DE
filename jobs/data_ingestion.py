import requests
from datetime import datetime, timedelta
import json

def data_ingestion(**kwargs):
    # calculate the date for the previous day
    execution_date = kwargs['execution_date']
    prev_execution_date = execution_date - timedelta(days=1)
    yesterday = prev_execution_date.strftime("%Y-%m-%d")

    # define the API endpoint
    url = "https://v1.basketball.api-sports.io/games"

    # specify the parameters for the API call
    params = {
        "date": yesterday
    }

    # make the API call
    response = requests.get(url, params=params)

    # check the status code of the response
    if response.status_code == 200:
        # retrieve the data from the API and convert it to json format
        data = response.json()
        # save the data to a file
        with open("data/raw/basketball_games_{}.json".format(yesterday), "w") as f:
            json.dump(data, f)
    else:
        print("Error:", response.status_code)