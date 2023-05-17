spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    spicy_list = [spicy_food["name"] for spicy_food in spicy_foods]

    return spicy_list
    pass


def get_spiciest_foods(spicy_foods):
    hotter_than_five = [
        spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
    return hotter_than_five


def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food["heat_level"]
        print(
            f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_level}")
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    pass


def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food["heat_level"]
        if spicy_food["heat_level"] > 5:
            print(
                f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {heat_level}")

    pass


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)

    for food in spicy_foods:
        total_heat_level += food["heat_level"]

    if num_foods > 0:
        average = total_heat_level / num_foods
        return int(average)
    else:
        return 0
    pass


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
