# TITLE: pysports_update_and_delete.py
# AUTHOR: Kevin Collins
# DATE: 2023-07-30
# DESCRIPTION: Tests insterting, updating, and deleting pysports database player records

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

# method for executing inner join on player and team tables
def show_players(cursor, title):

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # create variable for query results 
    players = cursor.fetchall()

    # display inner join query using for loop
    print("\n-- {} --".format(title))
    for player in players:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

# Try block to connect using config object. Display errors if they occur.
try:
    
    # Connect to DB using config object
    db = mysql.connector.connect(**config)
    
    # Create varialbe for performing queries
    cursor = db.cursor()

    # Insert player query 
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # Player data fields 
    player_data = ("Smeagol", "Shire Folk", 1)

    # Insert new player record
    cursor.execute(add_player, player_data)

    # Commit new player record 
    db.commit()

    # Show all player records after insert
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # Update the new player record 
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # Execute the player record update
    cursor.execute(update_player)

    # Show all player records after update
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # Delete player record 
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    # Execute player record delete
    cursor.execute(delete_player)

    # Show all player records after delete
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

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