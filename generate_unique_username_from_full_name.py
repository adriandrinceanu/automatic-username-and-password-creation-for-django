from django.contrib.auth import get_user_model


def generate_unique_username(first_name, last_name):
    # Create the initial username
    username = f"{first_name}_{last_name}".lower()
    # Ensure the username is unique
    User = get_user_model()
    counter = 0
    while User.objects.filter(username=username).exists():
        counter += 1
        username = f"{first_name}_{last_name}_{counter}".lower()
    return username


"""
Now, based on your models, you cand rewrite the save method so that when you add a new user, the username is autmatically assigned, for example:
first_name = Adrian 
last_name = Drinceanu
username will be adrian_drinceanu

Then with the save method rewritten, the password will be adrian_drinceanu, saving time for testing users in the development phase of your app.

"""

# def save_model(self, request, obj, form, change):
#         if not obj.user:  # if the user is being created for the first time
#             # Create a new user
#             username = generate_unique_username(obj.name)  
#             password = username
#             user = User.objects.create_user(username=username, password=password)
#             obj.user = user
#         obj.save()