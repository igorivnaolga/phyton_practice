class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color

first_animal = Animal("Buddy", 10)
second_animal = Animal("Ali", 8)
Animal.change_color("red")