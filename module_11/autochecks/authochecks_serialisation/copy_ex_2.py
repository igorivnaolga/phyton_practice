import pickle
from copy import copy, deepcopy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return self.__class__(self.name, self.email, self.phone, self.favorite)
        
    

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = self.__class__(self.filename, copy(self.contacts))
        copy_obj.is_unpacking = self.is_unpacking
        copy_obj.count_save = self.count_save
        return copy_obj
        
        

    def __deepcopy__(self, memo):
        copy_obj = self.__class__(self.filename, deepcopy(self.contacts))
        memo[id(copy_obj)] = copy_obj
        copy_obj.is_unpacking = self.is_unpacking
        copy_obj.count_save = self.count_save
        return copy_obj
    

p1 = Person("John Doe", "john@example.com", "+123456789", True)
p2 = Person("Jane Doe", "jane@example.com", "+987654321", False)

contacts = Contacts("contacts.pkl", [p1, p2])

# Створюємо копію
contacts_copy = copy(contacts)

print(contacts_copy.filename)  # "contacts.pkl"
print(contacts_copy.contacts)  # [p1, p2]
print(contacts_copy.is_unpacking)  # False
print(contacts_copy.count_save)  # 0