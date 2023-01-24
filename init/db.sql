CREATE SCHEMA IF NOT EXISTS basketball;

CREATE TABLE games (
    id INTEGER NOT NULL,
    date TIMESTAMP NOT NULL,
    time VARCHAR(5) NOT NULL,
    timestamp INTEGER NOT NULL,
    timezone VARCHAR(5) NOT NULL,
    stage INTEGER,
    week INTEGER,
    status_id INTEGER NOT NULL,
    league_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    home_team_id INTEGER NOT NULL,
    away_team_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (status_id) REFERENCES status(id),
    FOREIGN KEY (league_id) REFERENCES leagues(id),
    FOREIGN KEY (country_id) REFERENCES countries(id),
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id)
);

CREATE TABLE scores (
    id INTEGER NOT NULL,
    home_quarter_1 INTEGER NOT NULL,
    home_quarter_2 INTEGER NOT NULL,
    home_quarter_3 INTEGER NOT NULL,
    home_quarter_4 INTEGER NOT NULL,
    home_over_time INTEGER,
    home_total INTEGER NOT NULL,
    away_quarter_1 INTEGER NOT NULL,
    away_quarter_2 INTEGER NOT NULL,
    away_quarter_3 INTEGER NOT NULL,
    away_quarter_4 INTEGER NOT NULL,
    away_over_time INTEGER,
    away_total INTEGER NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE status (
    id INTEGER NOT NULL,
    long VARCHAR(20) NOT NULL,
    short VARCHAR(5) NOT NULL,
    timer INTEGER,
    PRIMARY KEY (id)
);


CREATE TABLE leagues (
id INTEGER NOT NULL,
name VARCHAR(50) NOT NULL,
type VARCHAR(50) NOT NULL,
season VARCHAR(20) NOT NULL,
logo VARCHAR(200) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE countries (
id INTEGER NOT NULL,
name VARCHAR(50) NOT NULL,
code VARCHAR(5) NOT NULL,
flag VARCHAR(200) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE teams (
id INTEGER NOT NULL,
name VARCHAR(50) NOT NULL,
logo VARCHAR(200) NOT NULL,
game_id INTEGER NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (game_id) REFERENCES games(id)
    PRIMARY KEY (id)
);
