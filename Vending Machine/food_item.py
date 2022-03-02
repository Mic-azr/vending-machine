# Class representing food items that would be found in a typical vending machine (soda, chips, etc.)
# Class objects will have str for name, str for type of food, and float for price USD
# Utilizes dataclass

from dataclasses import dataclass

@dataclass
class FoodItem:
    name: str #Name of food item, for example "Dungbitos", "Canned Pilk", "Fried Mothballs"
    food_type: str #Type of food, for example "soda" or "pretzels"
    price: float

    def print_food_item_info(self):
        print(f"{self.name:20}: {self.food_type:20}: ${self.price:5}") # Width of 20 for name and food_type, width of 5 for price as there shouldn't be any price higher than 99.99
