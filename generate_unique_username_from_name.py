from django.contrib.auth import get_user_model

def generate_unique_username_from_name(name):
    # Create the initial username
    name = name.replace(' ', '_')
    username = f"{name}".lower()
    # Ensure the username is unique
    User = get_user_model()
    counter = 0
    while User.objects.filter(username=username).exists():
        counter += 1
        username = f"{name}_{counter}".lower()
    return username

"""
Now, based on your models, you cand rewrite the save method so that when you add a new user, the username is autmatically assigned, for example:
name = Adrian Drinceanu
username will be adrian_drinceanu

Then with the save method rewritten, the password will be adrian_drinceanu, saving time for testing users in the development phase of your app.

"""

# def save_model(self, request, obj, form, change):
#         if not obj.user:  # if the user is being created for the first time
#             # Create a new user
#             username = generate_unique_username_from_name(obj.name)  
#             password = username
#             user = User.objects.create_user(username=username, password=password)
#             obj.user = user
#         obj.save()