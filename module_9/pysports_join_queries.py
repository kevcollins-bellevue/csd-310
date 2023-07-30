# TITLE: pysports_join_queries.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-30
# DESCRIPTION: Tests inner join queries for player and team tables

import mysql.connector
from mysql.connector import errorcode

# config object for MySQL credentials
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# Try block to connect using config object. Display errors if they occur.
try:
    
    # Connect to DB using config object
    db = mysql.connector.connect(**config)
    
    # Create varialbe for performing queries
    cursor = db.cursor()

    # Inner join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # create variable for query results 
    players = cursor.fetchall()

    # display inner join query using for loop
    print("\n-- DISPLAYING TEAM RECORDS --")
    for player in players: 
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

    # Prompt to close
    input("\n\n  Press any key to continue... ")
    
# Begin exception block
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
        
    else:
        print(err)
        
finally:
    # close MySQL connection
    db.close()