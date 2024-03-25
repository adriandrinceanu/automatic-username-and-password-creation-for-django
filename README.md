# Django Unique Username Generator with automatic simple password generator

This Python script is a utility for Django applications that generates a unique username from a given name. It's especially useful during the development phase of your app for testing users.

## How it Works

The script defines a function `generate_unique_username_from_name(name)` or `generate_unique_username(first_name, last_name)`, which takes a name as input, replaces spaces with underscores, and converts it to lowercase to form an initial username.

The function then checks if a user with the generated username already exists in the Django User model. If it does, the function appends a counter to the username and increments it until a unique username is found.

## Usage

You can use this function to automatically assign usernames when creating new users. For example, if the name is "Adrian Drinceanu", the username will be "adrian_drinceanu".

You can also rewrite the save method in your models to automatically assign the username and use it as the password when a new user is created. This can save time when testing users in the development phase of your app.

Here's an example of how you can do this:

```python
def save_model(self, request, obj, form, change):
    if not obj.user:  # if the user is being created for the first time
        # Create a new user
        username = generate_unique_username_from_name(obj.name)  
        password = username
        user = User.objects.create_user(username=username, password=password)
        obj.user = user
    obj.save()
