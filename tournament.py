#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except IOError:
        print ('Error! Could not connect to the tournament database. Have '
               'you set it up with "psql -f tournament.sql"?')
        return

        
def dbExecute(sqlString,data=None):
    """Takes a query statement as input and executes it. If the query 
    returns one or more tuples as results, yields a list of those tuples.
    Otherwise, returns None.
    
    Note that, to protect against SQL injection while still using 
    psycopg2 library, there is an optional second argument with data for
    parameterized queries. data should be a tuple so the calling statement
    dbExecute(sqlString,data) would be written much like psycopg2's 
    cursor.execute() method."""
    conn = connect()
    c = conn.cursor()
    if (data == None):
        c.execute(sqlString)
    else:
        c.execute(sqlString,data)
    # sqlString could be a command or a query
    try:
        if c.rowcount == 1:
            return c.fetchone()
        else:
            return c.fetchall()
    except psycopg2.ProgrammingError: # No results to fetch, it's a command
        conn.commit()
        return


def deleteMatches():
    """Remove all the match records from the database."""
    dbExecute('DELETE FROM matches;')


def deletePlayers():
    """Remove all the player records from the database."""
    dbExecute('DELETE FROM players;')


def countPlayers():
    """Returns the number of players currently registered."""
    res = dbExecute('SELECT COUNT(p_id) FROM players;')
    return res[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    dbExecute('INSERT INTO players (name) VALUES (%s);',(name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return dbExecute('SELECT * FROM standings;')


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    dbExecute('INSERT INTO matches (winner, loser) VALUES (%s, %s);', (winner,loser))
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    tmp = playerStandings()
    res = []
    # Assembles the response tuples (id1, name1, id2, name2) and 
    #    appends them to the res list
    res.extend([(tmp[i][0],tmp[i][1],
                 tmp[i+1][0],tmp[i+1][1]) 
                 for i in range(0, len(tmp), 2)])
    return res


