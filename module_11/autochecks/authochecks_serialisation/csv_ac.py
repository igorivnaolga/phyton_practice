import csv

def write_contacts_to_file(filename, contacts):
    """Записує список контактів у CSV-файл"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["name", "email", "phone", "favorite"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()  # Записуємо заголовки
        writer.writerows(contacts)  # Записуємо дані


def read_contacts_from_file(filename):
    """Читає список контактів із CSV-файлу та конвертує favorite у bool"""
    contacts = []
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            row["favorite"] = row["favorite"] == "True"  # Конвертуємо рядок у логічне значення
            contacts.append(row)
    
    return contacts


# 📌 **Приклад використання**
contacts = [
    {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
    {"name": "Chaim Lewis", "email": "dui.in@egetlacus.ca", "phone": "(294) 840-6685", "favorite": False},
    {"name": "Kennedy Lane", "email": "mattis.Cras@nonenimMauris.net", "phone": "(542) 451-7038", "favorite": True},
    {"name": "Wylie Pope", "email": "est@utquamvel.net", "phone": "(692) 802-2949", "favorite": False},
    {"name": "Cyrus Jackson", "email": "nibh@semsempererat.com", "phone": "(501) 472-5218", "favorite": True}
]

# ✅ Записуємо контакти у CSV
write_contacts_to_file("contacts.csv", contacts)

# ✅ Зчитуємо контакти назад
loaded_contacts = read_contacts_from_file("contacts.csv")
print(loaded_contacts)
