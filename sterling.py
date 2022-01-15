'''
TODO Create a map and filter function based on scenarios
    Sterling's Scenario:
You could use map to display all of the game scores for the blazers this season. 
And you could use filter to only display the games when they scored over 100 points.
'''

scores = [
    {
        "date": "Jan 13, 2022",
        "opp": "Denver Nuggets",
        "blazer_score": 108,
        "opp_score": 140
    },
    {
        "date": "Jan 10, 2022",
        "opp": "Brooklyn Nets",
        "blazer_score": 114,
        "opp_score": 108
    },
    {
        "date": "Jan 9, 2022",
        "opp": "Sacramento Kings",
        "blazer_score": 99,
        "opp_score": 88
    },
]


def display_scores(scores):
    list(map(lambda score: print("Your Portland Trailblazers: ",
                                 score["blazer_score"], ",", score["opp"], score["opp_score"]), scores))


display_scores(scores)

only_hundred = filter(lambda score: score.get("blazer_score") > 100, scores)
print("Games Blazers scored over 100: ", list(only_hundred))
