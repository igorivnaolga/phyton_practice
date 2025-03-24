import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"Person(name={self.name}, email={self.email}, phone={self.phone}, favorite={self.favorite})"
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        self.contacts = contacts 
        if contacts is None:
            contacts = []
        
        

    def save_to_file(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self, f)
        
            

    def read_from_file(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
        

contacts = [
    Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False),
    Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", False),
    Person("Kennedy Lane", "mattis.Cras@nonenimMauris.net", "(542) 451-7038", True),
]

# ✅ Створюємо об'єкт Contacts
contact_list = Contacts("contacts.pkl", contacts)

# ✅ Зберігаємо весь об'єкт Contacts у файл
contact_list.save_to_file()

# ✅ Зчитуємо об'єкт Contacts з файлу
loaded_contact_list = Contacts.read_from_file("contacts.pkl")

# Перевіряємо, що дані збережені правильно
print(loaded_contact_list.contacts)