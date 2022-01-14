'''
TODO Create a map and filter function based on scenarios
    Masa's Scenario:
    map: give suggested usernames to a new signup
    filter: verify if a username is already taken
'''

# imports
import random

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

new_signup = {
    "name": "Masa Kawaharada",
    "username": "Masa80"
}

user1 = new_signup["name"].split(" ")
print(user1[1][:1])
# user1 = reduce(lambda x,y: x+y, user1[0:1])

user2 = new_signup["name"].replace(" ", "_")

print(random.randint(100, 1000))
print(user2)


def checker(username, exist_usernames):
    username_taken = filter(
        lambda usernames: usernames.get("username"), exist_usernames)
    print('this username is taken: ', list(username_taken))

    if username_taken:
        return True
    return False


print(checker(exist_usernames, new_signup["username"]))
