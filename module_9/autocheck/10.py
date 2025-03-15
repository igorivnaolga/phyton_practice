from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return sum(1 for char in self.data if char.isdigit())