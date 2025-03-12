# class Owner:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone

#     def info(self):
#         return f"{self.name}: {self.phone}"

# class Cat(Owner):
#     def __init__(self, nickname, age, name, phone):
#         super().__init__(name, phone)
#         self.nickname = nickname
#         self.age = age

#     def cat_info(self):
#         return f"Cat Name: {self.nickname}, Age: {self.age}"

# 		def sound(self):
# 		        return "Meow"

# cat = Cat('Simon', 4, 'Boris', '+380503002010')
# print(cat.info())
# print(cat.cat_info())



class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"

owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print(cat.owner.info())
print(cat.get_info())
