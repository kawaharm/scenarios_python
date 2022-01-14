# menu = {
#     "breakfast": ['pancakes', 'waffles'],
#     "lunch": ['hot dog', 'hamburger'],
#     "dinner": ['steak', 'fish and chips'],
#     "drinks": ['cola', 'sprite', 'coffee'],
# }
 
# ==========Map========== #

breakfast_menu = ['pancakes', 'waffles', 'eggs']
lunch_menu = ['hot-dog', 'hamburger', 'pizza']
dinner_menu = ['steak', 'fish and chips', 'roast chicken']
drink_menu = ['cola', 'sprite', 'coffee']
 
def make_a_meal(x,y,z,a):
   return x + ", " + y + ", " + z + ", and " + a
 
meal_one = map(make_a_meal, breakfast_menu, lunch_menu, dinner_menu, drink_menu)
print("Meal 1", list(meal_one))
 
meal_two = map(lambda x, y: x + y, lunch_menu, drink_menu)
print("I want a ", str(list(meal_two)))

# ==========Filter========== #

# man what is this 