'''
TODO Create a map and filter function based on scenarios
    Kyle's Scenario:
use a map to have list of business's
filter to list phone numbers
'''

# Map

businesses = [
    {
        "name": "McDonalds",
        "number": 1234567
    },
    {
        "name": "Taco Bell",
        "number": 7777777
    },
    {
        "name": "Burger King",
        "number": 100000
    },
]

names_list = map(lambda name: name["name"], businesses)
print(list(names_list))

# Filter

numbers_list = filter(lambda number: number["number"], businesses)
print(list(map(lambda x: x["number"], numbers_list)))
