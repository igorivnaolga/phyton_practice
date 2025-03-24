import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None, count_save: int = 0):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = count_save
        self.is_unpacking = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(filename):
        with open(filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __setstate__(self, value):
        self.__dict__.update(value)
        self.is_unpacking = True


contacts = [
    Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
    Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
    Person("Kennedy Lane", "mattis.Cras@nonenimMauris.net", "(542) 451-7038", True),
]

# ✅ Створюємо об'єкт Contacts
contact_list = Contacts("contacts.pkl", contacts)

# ✅ Зберігаємо його у файл
contact_list.save_to_file()

# ✅ Завантажуємо назад
loaded_contact_list = Contacts.read_from_file("contacts.pkl")

# ✅ Перевіряємо дані
print(loaded_contact_list.contacts)
print("Кількість збережень:", loaded_contact_list.count_save)
print("is_unpacking:", loaded_contact_list.is_unpacking)