from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages
# from datetime import datetime
# from time import strftime, strptime


# Create your views here.
     

def index(request):
    return render(request, 'login-reg.html')

def display_login(request):
    return redirect('/')

def create_user(request):
# if request method is GET then redirect to log in page

# if request method is POST then check errors. If no errors, move on to create user
    if request.method == "POST":
        print("request.POST:",request.POST)
        # to check errors before creating users. Display message amd redirect to log in page if there're errors:
        errors = User.objects.basic_validator(request.POST, "reg_login")

        if len(errors) > 0:
            print("errors: ",errors)
            for key, val in errors.items():
                messages.error(request, val)
            return redirect("/")

        # user will be created if there's no validation errors:
        print("----------Start creating user")

        hashed_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        created_user = User.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"], password = hashed_pw)
        
        request.session["user_id"] = created_user.id

        return redirect("/user/books")
    
    # if request method is GET then redirect to log in page
    return redirect("/")

def login(request):
    if request.method == "POST":
        #try to find the user in the DB
        potential_users = User.objects.filter(email = request.POST["email"])

        if len(potential_users) ==0:
            messages.error(request, "Please check your email and password.")
            return redirect('/')
        
        #if we're here, meaning the email was found.
        #compate the provided pw with the hashed on in the DB
        if bcrypt.checkpw(
            request.POST["password"].encode(),
            potential_users[0].password.encode()):
            request.session["user_id"] = potential_users[0].id
            return redirect("/user/books")
        
        #if we're here, the password was incorrect
        messages.error(request, "Please check your email and password.")
    return redirect("/user/books")

def logout(request):
    request.session.clear()
    return redirect("/")

def display_all_books(request):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect("/")
    context = {
        "current_user": User.objects.get(id=request.session["user_id"]),
        "all_books": Book.objects.all(),
    }
    return render(request, 'all_books.html', context)

def display_my_fav_books(request):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect("/")
    context = {
        "current_user": User.objects.get(id=request.session["user_id"]),
    }
    return render(request, 'my_books.html', context)

def add_book(request):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect("/")
    
    if request.method == "POST":
        print("request.POST:",request.POST)
        # to check errors before adding book to db. Display message amd redirect to all books page if there're errors:
        errors = User.objects.basic_validator(request.POST, "add_book")

        if len(errors) > 0:
            print("errors: ",errors)
            for key, val in errors.items():
                messages.error(request, val)
            return redirect("/")
        current_user = User.objects.get(id=request.session["user_id"])
        created_book = Book.objects.create(tittle=request.POST["tittle"], desc=request.POST["desc"], uploaded_by_id=current_user.id)
        created_book.users_who_like.add(current_user)
    return redirect('/user/books')

def display_book_info(request, book_id):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect("/")
    context = {
        "current_user": User.objects.get(id=request.session["user_id"]),
        "all_books": Book.objects.all(),
        "this_book": Book.objects.get(id=book_id),
        'book_id': book_id,
    }
    return render(request, 'book_info.html', context)
    

def update_my_book(request, book_id):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect('/')
    if request.method == "POST":
        print("request.POST:",request.POST)
        # to check errors before updating book in db. Display message amd redirect to all books page if there're errors:
        errors = User.objects.basic_validator(request.POST, "add_book")

        if len(errors) > 0:
            print("errors: ",errors)
            for key, val in errors.items():
                messages.error(request, val)
            return redirect(f"/user/edit-book-input/{book_id}")
        book_to_update = Book.objects.get(id=book_id)
        book_to_update.tittle = request.POST["tittle"]
        book_to_update.desc = request.POST["desc"]
        book_to_update.save()

    return redirect(f"/user/edit-book-input/{book_id}")

def delete_book(request, book_id):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect('/')
    if request.method == "POST":
        Book.objects.get(id=book_id).delete()
    return redirect('/user/books')


def update_fav_book(request, book_id):
    # to redirect to log in page when user didn't log an and user typed the direct path in the site address
    if "user_id" not in request.session:
        messages.error(request, "You need to log in to see that page.")
        return redirect('/')
    
    if request.method == "POST":
        current_user= User.objects.get(id=request.session["user_id"])
        this_book= Book.objects.get(id=book_id)

        if current_user not in this_book.users_who_like.all():
            print("This book wasn't user's favorite")
            this_book.users_who_like.add(current_user)
            print("is this book now user's favorite?", current_user in this_book.users_who_like.all())
        else:
            print("This book was user's favorite")
            this_book.users_who_like.remove(current_user)
            print("is this book now user's favorite?", current_user in this_book.users_who_like.all())
        this_book.save()
    
    return redirect(request.META.get('HTTP_REFERER'))
    