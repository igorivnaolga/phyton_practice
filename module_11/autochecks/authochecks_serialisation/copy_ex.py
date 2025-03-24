import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"Person(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"


def copy_class_person(person):
    return copy.copy(person)

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


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)
    

original_person = Person("John Doe", "john.doe@example.com", "+123456789", True)
copied_person = copy_class_person(original_person)

# ✅ Переконуємося, що це окрема копія
print(original_person)  # Person(name=John Doe, email=john.doe@example.com, phone=+123456789, favorite=True)
print(copied_person)    # Person(name=John Doe, email=john.doe@example.com, phone=+123456789, favorite=True)

# ✅ Перевіряємо, що це різні об'єкти
print(original_person is copied_person)  # False (вони різні об'єкти)