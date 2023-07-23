# TITLE: mysql_test.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-23
# DESCRIPTION: Tests queries for the pysports database

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

    # select the team_id , team_name, and mascot from the team table
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # create variable for team cursor results 
    teams = cursor.fetchall()

    # display team query using for loop
    print("\n-- DISPLAYING TEAM RECORDS --")
    for team in teams: 
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    # select the player_id, first_name, last_name, and team_id from the player table
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # create variable for player cursor results 
    players = cursor.fetchall()

    # display player query using for loop
    print ("\n-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

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
    db.close()