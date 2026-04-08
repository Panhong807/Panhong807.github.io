# This script defines a FoodItem class to represent food items with their nutrition data, and a nutrition_tracker function that takes a list of FoodItem objects, calculates the total nutrition summary, and prints warnings if certain limits are exceeded.
class FoodItem(object):
    """
    Class representing a food item with nutrition data
    """

    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
def nutrition_tracker(food_list):
    """
    Input: list of FoodItem objects
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

apple = FoodItem("Apple", 60, 0.3, 15, 0.5)
burger = FoodItem("Burger", 500, 25, 40, 20)
pizza = FoodItem("Pizza", 800, 30, 90, 35)
food_list = [apple, burger, pizza]
nutrition_tracker(food_list)