/*Insert store records*/
INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

/*Insert book records*/
INSERT INTO book(book_name, author, details)
    VALUES('Foundation', 'Isaac Asimov', 'The first book in the Foundation trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Foundation and Empire', 'Isaac Asimov', 'The second book in the Foundation trilogy');

INSERT INTO book(book_name, author, details)
    VALUES('Second Foundation', 'Isaac Asimov', 'The third book in the Foundation trilogy');

INSERT INTO book(book_name, author)
    VALUES('Spin', 'Robert Charles Wilson');

INSERT INTO book(book_name, author)
    VALUES('Anathem', 'Neal Stephenson');

INSERT INTO book(book_name, author)
    VALUES('The Devil in the White City', 'Erik Larson');

INSERT INTO book(book_name, author)
    VALUES("King Leopold's Ghost", 'Adam Hochschild');

INSERT INTO book(book_name, author)
    VALUES('Survivor', 'Chuck Palahniuk');

INSERT INTO book(book_name, author)
    VALUES('Salt Fat Acid Heat', 'Samin Nosrat');
	
/*Insert user records*/
INSERT INTO user(first_name, last_name) 
    VALUES('Spike', 'Spiegel');

INSERT INTO user(first_name, last_name)
    VALUES('Faye', 'Valentine');

INSERT INTO user(first_name, last_name)
    VALUES('Jet', 'Black');
	
/*Insert wishlist records where FK values equal user first_name and book book_name PK IDs*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Spike'), 
        (SELECT book_id FROM book WHERE book_name = 'Foundation')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Faye'),
        (SELECT book_id FROM book WHERE book_name = 'The Devil in the White City')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jet'),
        (SELECT book_id FROM book WHERE book_name = 'Salt Fat Acid Heat')
    );
