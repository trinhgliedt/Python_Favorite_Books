from django.urls import path

from . import views

urlpatterns = [

    path('', views.index), #GET, redirect to root
    path('user', views.display_login), #GET, redirect to root
    path('user/create-user', views.create_user), # 1.POST: create new user --> output: user/messages. 2. GET: redirect to root
    path('user/login', views.login), # 1. POST, log user in --> output: user/messages. 2. GET: redirect to root
    path('user/logout', views.logout), # 1. POST, log user out (clear user_id from session) --> output: redirect to root. 2. GET: redirect to root
    #page 2
    path('user/books', views.display_all_books), #GET: if user is not logged in: redirect to root. If user is logged in, render all_books.html (which includes input form to add a fav book)
    
    path('user/add-book', views.add_book), #GET: if user is not logged in: redirect to root. If user is logged in, redirect to user/books 
    #POST: process form to add a book to db. Then redirect to user/books 
    
    #sensei bonus
    path('user/fav-books', views.display_my_fav_books),#GET: if user is not logged in: redirect to root. If user is logged in, render my_books.html 
    
    #page 3
    path('user/edit-book-input/<int:book_id>', views.display_book_info), #GET: if user is not logged in: redirect to root. If user is logged in, render book_info.html (which includes input form to edit book and un-favorite the book)
    path('user/update-book/<int:book_id>',views.update_my_book),#GET: if user is not logged in: redirect to root. If user is logged in, redirect to user/edit-book-input/<book_id>
    #POST: process form to update book in db. Then redirect to user/edit-book-input/<book_id>
    path('user/book/<book_id>/delete',views.delete_book),#GET: if user is not logged in: redirect to root. If user is logged in, redirect to book info.
    #POST: process deletion of the book. Then redirect to user/books

    #page 4
    path('user/show-book/<int:book_id>', views.display_book_info), #GET: if user is not logged in: redirect to root. If user is logged in, render book_info.html (which includes input form mark book as favorite)
    path('user/update-fav-book/<int:book_id>', views.update_fav_book),#GET: if user is not logged in: redirect to root. If user is logged in, redirect to user/fav-book/<book_id>
    #POST: process form to enable the link of the many to many key (users_who_like). Then redirect user/fav-book/<book_id>
]