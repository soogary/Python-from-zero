def my_worker(fruit):
    statement = f"My fave meal is chicken and {fruit}"
    meals = {"dinner": statement}
    return meals

meal = my_worker("lemon")