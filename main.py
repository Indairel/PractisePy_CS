class Broth:
    def __init__(self):
        self.cook_time = "Kolme tuntia"
        self.ingredients()
        self.__onion = "polta sitä ennen lisäämistä"
        # Private attribute - will not be displayed when call - P.S. it`s not private
    def ingredients(self):
        print("Pasta, liha, vihannekset, sipuli, suola")
    def __secret(self):
        print("Keitto ei maistu niin hyvältä, jos et", self._Broth__onion, "!")

class Tomato_Soup(Broth):
    def __init__(self):
        super().__init__()
        self.cook_time = "Kaksi tuntia"
    def add_new_ingredient(self):
        print("Pasta, liha, vihannekset, sipuli, suola, tomaatti")


cooking_soup = Tomato_Soup()
# print("Tomato soup cook time:", cooking_soup.cook_time)
# print("Broth cook time:", Broth().cook_time)
# print(cooking_soup._Tomato_Soup__cost)
cooking_soup._Broth__secret()
