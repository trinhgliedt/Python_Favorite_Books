from django.db import models
import re


# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, post_data, page):
        errors = {}
        if page == "reg_login":
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+[a-zA-Z]+$')

            if len(post_data["first_name"]) < 2:
                errors["first_name"] = "Please enter at least 2 characters for your first name."
            if len(post_data["last_name"]) < 2:
                errors["last_name"] = "Please enter at least 2 characters for your last name."
            if not EMAIL_REGEX.match(post_data['email']): 
                errors['email'] = 'Please enter a valid email address!'
            elif User.objects.filter(email = post_data["email"]).exists():
                errors['email'] = "You can't use that email address."
            if len(post_data["password"]) < 3:
                errors["password"] = "Please provide a password of at least 3 characters"
            if post_data["password"] != post_data["confirmPW"]:
                errors["confirmPW"] = "Please ensure that your password matches the confirmation."

        if page == "add_book":
            if len(post_data["tittle"]) < 1:
                errors["tittle"] = "Please enter a tittle for the book."
            if len(post_data["desc"]) < 5:
                errors["desc"] = "Please enter at least 5 characters for the book description."

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    #fav_books = a list of books liked by a given user
    #books_uploaded = a list of books uploaded by a given user

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()


class Book(models.Model):
    tittle = models.CharField(max_length=255)
    desc = models.TextField()

    uploaded_by = models.ForeignKey(
        User,
        related_name='books_uploaded',
        on_delete=models.CASCADE)

    users_who_like = models.ManyToManyField(
        User,
        related_name='fav_books')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
