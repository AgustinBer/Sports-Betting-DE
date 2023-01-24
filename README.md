
# Data Pipeline for Basketball Games

This project is a data pipeline for extracting, cleaning, and validating information about basketball games from an API. The pipeline is built using Airflow and the data is stored in Redshift.

## Architecture 

![alt text](https://i.gyazo.com/eab6ff1bd780ab0da3a221293e22a6be.png)

## ERD Diagram

![alt text](https://i.gyazo.com/5bd85b3c0f895662a614031d326bce14.png)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
The following packages need to be installed:

- airflow
- pandas
- json
- requests
- great_expectations
- sqlalchemy
- psycopg2

## Installing
Clone the repository and install the packages:
```
git clone https://github.com/<username>/data-pipeline-basketball-games.git
pip install -r requirements.txt
```

Setting up the environment
Create a .env file in the root of the project with the following variables:

```
REDSHIFT_USER
REDSHIFT_PASSWORD
REDSHIFT_DB
REDSHIFT_HOST
REDSHIFT_PORT
```

## Running the pipeline
To run the pipeline, use the following command:
```
airflow run <DAG_ID> <TASK_ID> <EXECUTION_DATE>
```
## Built With
- Airflow - Data orchestration
- Pandas - Data manipulation
- Great Expectations - Data validation
- Redshift - Data storage

## Authors
Agustin Bergoglio

