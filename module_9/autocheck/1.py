class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
    def say(self):
        return f"Nickname: {self.nickname}, weight: {self.weight}"

animal = Animal("Buddy", 10)
    