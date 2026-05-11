# This script defines a food_item class to represent food items with their nutrition data,
# and a nutrition_tracker function that calculates daily totals and prints warnings when needed.


class food_item(object):
    """
    Class representing a food item with nutrition data.
    """

    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


FoodItem = food_item


def nutrition_tracker(food_list):
    """
    Input: list of food_item objects
    Returns: total nutrition summary
    Prints warning if limits exceeded
    """
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    print("Total calories:", total_calories)
    print("Total protein:", total_protein)
    print("Total carbs:", total_carbs)
    print("Total fat:", total_fat)

    if total_calories > 2500:
        print("Warning: Excess calorie intake!")

    if total_fat > 90:
        print("Warning: Excess fat intake!")

    return total_calories, total_protein, total_carbs, total_fat


apple = food_item("Apple", 60, 0.3, 15, 0.5)
burger = food_item("Burger", 500, 25, 40, 20)
pizza = food_item("Pizza", 800, 30, 90, 35)
food_list = [apple, burger, pizza]
nutrition_tracker(food_list)
