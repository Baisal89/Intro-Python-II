 class Item:
     def __init__(self, name, description):
         self.name = name
         self.description = description

class Food(Item):
    


class Egg(Food):
    def __init__(self):
        super().__init__("egg", "This is an egg", 20)


def __init__(self, name, description, calories):
    super().__init__(name, description)
    self.calories = calories
