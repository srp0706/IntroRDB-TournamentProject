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
CREATE TABLE players (pid serial primary key, name text not null);
CREATE TABLE matches (mid serial primary key, winner integer, loser integer);
CREATE VIEW standings as select pid, (select count(winner) from matches where winner = players.pid) as wins, (select count(mid) from matches where winner = players.pid or loser = players.pid) as plays from players;

-- Extra credit
-- CREATE TABLE tournament (tid integer primary key, tname text)
