# TITLE: whatabook.py
# AUTHOR: Kevin Collins
# DATE: 2023-08-12
# DESCRIPTION: WhatABook program for final project.

import mysql.connector
from mysql.connector import errorcode

# Menu function
def menu():
    
    print('\n--- MENU OPTIONS ---')
    print('1. View Books')
    print('2. Store Locations')
    print('3. My Account')
    print('4. Exit Program')
    
    # Get menu choice
    while True:
        
        menu_choice = int(input('\nEnter a menu option number (1-4): '))
        
        if menu_choice in range(1, 5):
            return menu_choice
        
        else:
            print('\nInvalid number...\n')
            
# Function for querying book listings
def books_query(cursor):
    
    # Select book_id, book_name, auhor, and details from book
    cursor.execute('SELECT book_id, book_name, author, details FROM book')

    # Get book results from cursor
    books = cursor.fetchall()

    # Display book listings
    print('\n--- BOOK LISTINGS ---')
    for book in books:
        print('Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n'.format(book[0], book[1], book[2], book[3]))
        
# Function for querying store locations
def store_locations(cursor):
    
    # Select store_id and locale from store
    cursor.execute('SELECT store_id, locale FROM store')

    # Get location results from cursor
    locations = cursor.fetchall()

    print('\n--- STORE LOCATIONS ---')
    for location in locations:
        print('Store ID: {}\nLocale: {}\n'.format(location[0], location[1]))
        
# Function for getting and validating user_id
def validate_user():

    while True:
        
        user_id = int(input('\nEnter a User ID (1, 2, or 3): '))
        
        if user_id in range(1, 4):
            return user_id
        
        else:
            print('\nInvalid User ID...\n')

# Funtion for My Account menu option selection
def account_menu():

    print('--- ACCOUNT OPTIONS ---')
    print('1. Wishlist')
    print('2. Add Book')
    print('3. Return to Main Menu')
        
    while True:
        
        account_menu_choice = int(input('\nEnter a menu option number (1-3): '))
        
        if account_menu_choice in range(1, 4):
            return account_menu_choice
        
        else:
            print('\nInvalid option...\n')

# Function for querying wishlist contents            
def wishlist_contents(cursor, user_id):

    # Inner join query
    cursor.execute('SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author ' + 
                    'FROM wishlist ' + 
                    'INNER JOIN user ON wishlist.user_id = user.user_id ' + 
                    'INNER JOIN book ON wishlist.book_id = book.book_id ' + 
                    'WHERE user.user_id = {}'.format(user_id))
    
    # Get wishlist results from cursor
    wishlist = cursor.fetchall()

    print('\n--- WISHLIST CONTENTS ---')
    for book in wishlist:
        print('Book Name: {}\nAuthor: {}\n'.format(book[4], book[5]))

# Function for displaying available books        
def available_books(cursor, user_id):

    # Query books not in user's wishlist
    cursor.execute('SELECT book_id, book_name, author, details ' +
                   'FROM book ' +
                   'WHERE book_id ' +
                   'NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})'.format(user_id))

    books_available = cursor.fetchall()

    print('\n--- AVAILABLE BOOKS ---')

    for book in books_available:
        print('Book ID: {}\nBook Name: {}\nAuthor: {}\nDetails: {}\n'.format(book[0], book[1], book[2], book[3]))

# Function to add books to wishlist
def add_to_wishlist(cursor, user_id, book_id):
    
    # Insert values into wishlist
    cursor.execute('INSERT INTO wishlist(user_id, book_id) ' +
                   'VALUES({}, {})'.format(user_id, book_id))
    
    # Commit changes to database
    db.commit()

# Database config
config = {
    'user': 'whatabook_user',
    'password': 'MySQL8IsGreat!',
    'host': '127.0.0.1',
    'database': 'whatabook',
    'raise_on_warnings': True
}

# Begin try/catch block for database connection and query errors
try:
    
    # Connect to DB using config object
    db = mysql.connector.connect(**config)
    
    # Create varialbe for performing queries
    cursor = db.cursor()

    # Variable for user's selected menu option
    menu_selection = menu()
    
    # While the menu selection is not 4 (exit program)
    while menu_selection != 4:
        
        # If user selects 1, call books_query
        if menu_selection == 1:
            books_query(cursor)

        # If user selects 2, call store_locations
        elif menu_selection == 2:
            store_locations(cursor)

        # If user selects 3, call validate_user to get user_id, and account_menu to display account options
        elif menu_selection == 3:
            user_id = validate_user()
            account_menu_selection = account_menu()

            # While account_menu_selection is not 3 (return to main menu)
            while account_menu_selection != 3:

                # If user selects 1, call wishlist_contents
                if account_menu_selection == 1:
                    wishlist_contents(cursor, user_id)

                # If user selects 2, call available_books,
                # prompt user to enter book_id to add,
                # and call add_to_wishlist
                elif account_menu_selection == 2:

                    # show the books not currently configured in the users wishlist
                    available_books(cursor, user_id)

                    # get the entered book_id 
                    book_id_selection = int(input("\nEnter the Book ID you want to add: "))
                    
                    # add the selected book the user's wishlist
                    add_to_wishlist(cursor, user_id, book_id_selection)

                    print('\nBook ID: {} was added to your wishlist\n'.format(book_id_selection))

                # Show the account menu 
                account_menu_selection = account_menu()
        
        # Show the main menu
        menu_selection = menu()

    print('\n\nExiting program...')

# Handle errors
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The database does not exist')

    else:
        print(err)

# Close database connection
finally:
    db.close()