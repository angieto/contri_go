from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1 or len(postData['last_name']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1 or len(postData['password_confirm']) < 1:
            errors['missing_field'] = "All fields are required!"
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors['name_length'] = "Name must contain at least 2 characters"
        if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
            errors['non-alphabetical_name'] = "Name must include alphabetical characters only"
        try:
            validate_email(postData['email'])
        except: 
            errors['invalid_email'] = "Invalid email format!"
        if User.objects.filter(email=postData['email']):
            errors['duplicated_email'] = "This email address already exists!"
        if len(postData['password']) < 8:
            errors['password_length'] = "Password must contain at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors['invalid_confirm'] = "Passwords don't match"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email']) 
        if len(postData['email']) < 1 or len(postData['password']) < 1:
            errors['missing_fields'] = "All fields are required!"
        try:
            User.objects.get(email=postData['email']) 
        except User.DoesNotExist:
            errors['email'] = "No user found"
        if len(user) == 1:
            if not bcrypt.checkpw(postData['password'].encode('utf8'), user[0].password.encode('utf8')):
                errors['invalid_pw'] = "Invalid password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()


