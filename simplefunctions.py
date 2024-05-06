def my_worker(fruit):
    statement = f"My fave meal is {fruit} chicken"
    meals = {"dinner": statement}
    return meals

meal = my_worker("lemon")
meal.keys()

# function calling a subfunction

def human(food):
    consume = food["dinner"]
    return consume

my_meal=human(meal)
print(f"i want my meal. It will be:{my_meal}")


# another function