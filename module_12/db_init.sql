/*
	TITLE: whatabook_init.sql
	AUTHOR: Kevin Collins
	DATE: 2023-08-12
	DESCRIPTION: WhatABook initialization script.
*/

/* drop and create whatabook db*/
DROP DATABASE whatabook;
CREATE DATABASE whatabook;
USE whatabook

/*create user for whatabook db*/
DROP USER 'whatabook_user'@'localhost';
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

/*drop tables if they exist*/
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*create store table*/
CREATE TABLE store (
  store_id INT NOT NULL AUTO_INCREMENT,
  locale VARCHAR(500) NOT NULL,
  PRIMARY KEY (store_id)
);

/*create book table*/
CREATE TABLE book (
  book_id INT NOT NULL AUTO_INCREMENT,
  book_name VARCHAR(200) NOT NULL,
  author VARCHAR(200) NOT NULL,
  details VARCHAR(500),
  PRIMARY KEY (book_id)
);

/*create user table*/
CREATE TABLE user (
  user_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(75) NOT NULL,
  last_name VARCHAR(75) NOT NULL,
  PRIMARY KEY (user_id)
);

/*create wishlist table*/
CREATE TABLE wishlist (
  wishlist_id INT NOT NULL AUTO_INCREMENT,
  user_id INT NOT NULL,
  book_id INT NOT NULL,
  PRIMARY KEY (wishlist_id),
  FOREIGN KEY (user_id) REFERENCES user(user_id),
  FOREIGN KEY (book_id) REFERENCES book(book_id)
);

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
