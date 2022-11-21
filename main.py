class Broth:
    def __init__(self):
        self.cook_time = "Kolme tuntia"
        self.ingredients()
    def ingredients(self):
        print("Pasta, liha, vihannekset, sipuli, suola")

class Tomato_Soup(Broth):
    def __init__(self):
        super().__init__()
        self.cook_time = "Kaksi tuntia"
    def add_new_ingredient(self):
        print("Pasta, liha, vihannekset, sipuli, suola, tomaatti")

cooking_soup = Tomato_Soup()
print("Tomato soup cook time:", cooking_soup.cook_time)
print("Broth cook time:", Broth().cook_time)

