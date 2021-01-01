# Python_Favourite_Books
A website where users can upload their favorite books and other users on the website can indicate whether that book is also one of their favorites.

LThe two distinct relationships between the users and books tables are:
- One is a one-to-many relationship because a user can upload many books, and a book can be uploaded by one user. In the database, the uploaded_by_id field (in the books table) stores this relationship. 
- The second relationship is a many-to-many relationship, where a given user can like many books, and a given book can be liked by many users. This relationship is stored in the third table. (In the diagram, this is the likes table.)

Functionalities:
- [x] Create the User and Book models with all appropriate relationships
- [x] Incorporate a validated login/registration page
- [x] On the main page, allow the user to add a new book, with validations. Added books should automatically be favorited by the logged in user.
- [x] Have a list of all the books on the main page displaying the title and the user who uploaded the book
- [x] When the title is clicked, display a page with the book's information, including a list of all users who have favorited that book
- [x] If the logged in user has favorited the book, they should be able to "un-favorite" the book
- [x] If the logged in user has not yet favorited the book, there should be a link to add this book to their favorites
- [x] If the logged in user is the uploader of the book, allow them to edit (same validations apply) or delete the book
- [x] On the main page, if the logged in user has not favorited the book, there should be a link so the user can add it to their favorites. Otherwise, display a message indicating the book has already been favorited.
- [x] Add a user page that allows the user to view a list of all their favorite books


![](ERD.JPG)

![](main_view.png)
