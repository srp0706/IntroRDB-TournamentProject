-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Delete database if it exists
DROP DATABASE IF EXISTS tournament;

-- Create the database and connect to it
CREATE DATABASE tournament;
\c tournament

-- Create the tables
CREATE TABLE players (
     p_id  SERIAL  PRIMARY KEY,
     name  TEXT    NOT NULL);
CREATE TABLE matches (
     m_id   SERIAL   PRIMARY KEY, 
     winner INTEGER  REFERENCES players(p_id), 
     loser  INTEGER  REFERENCES players(p_id));
CREATE VIEW standings AS 
    SELECT p_id,
           name,
           (SELECT COUNT(winner)
              FROM matches 
             WHERE winner = players.p_id) 
                AS wins,
           (SELECT COUNT(m_id)
              FROM matches 
             WHERE winner = players.p_id OR loser = players.p_id) 
                AS plays 
      FROM players
     ORDER BY wins DESC;

-- Extra credit
-- CREATE TABLE tournament (tid integer primary key, tname text)
