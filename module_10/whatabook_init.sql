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
