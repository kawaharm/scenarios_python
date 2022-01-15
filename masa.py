'''
TODO Create a map and filter function based on scenarios
    Masa's Scenario:
    map: give suggested usernames to a new signup
    filter: verify if a username is already taken
'''

# imports
import random

# ***** Map *****
new_signup = {
    "name": "Kalanianaole Kamakana-Ali'i",
    "DOB": "February 30, 1992",
    "email": "humuhumunukunukuapua'a@email.com"
}

# Split first and last name
user1 = new_signup["name"].split(" ")

# Remove all but first character of last name
user1[1] = user1[1][:1]

# Join first and modified last name
user1 = "_".join(user1)

# Create 5 suggested usernames by adding random numbers after
new_usernames = [user1] * 5
sugg_usernames = map(lambda username: username +
                     str(random.randint(100, 1000)), new_usernames)

# Print 5 suggested usernames
print('Here are some suggested usernames for you: ', list(sugg_usernames))


# ***** Filter *****
# existing accounts
exist_usernames = [
    {
        "name": "Masaru Kawaharada",
        "username": "Masa808"
    },
    {
        "name": "Masa Kawa",
        "username": "Masa_K777"
    },
]

# New account
newer_signup = {
    "name": "Joe Biron",
    "username": "Masa_K777"
}

# Create an list that appends the new account's username if it is already taken
taken_username = list(filter(
    lambda user: user["username"] == newer_signup["username"], exist_usernames))

# If the list is empty, then the username is not taken
if not taken_username:
    print("this username is not taken. Have at it buddy!")
else:
    print("This username is taken. Sucks to suck!")


# print("hey")
