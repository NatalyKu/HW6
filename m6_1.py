from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str):
        if len(value) == 10 and value.isdigit() == True:
            super().__init__(value) 
        else:
            raise ValueError  
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None             
    
    def remove_phone(self, phone):
        if self.find_phone(phone):
            self.phones= [p for p in self.phones if p.value != phone]
        else:
            raise ValueError
   
    
    def edit_phone(self, phone, new_phone):
        if self.find_phone(phone):
            self.add_phone(new_phone)
            self.remove_phone(phone)
        else:
            raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data   

    def find(self, name):
        return self.data.get(name)
        
    
    def delete(self, name):
        if self.find(name):
            self.data.pop(name) 
            return "Record deleted"
        else:
            raise ValueError
    
    def __str__(self):
        records ='\n'.join(str(record) for record in self.data.values())
        return f"AddressBook:\n{records}"


book = AddressBook()
rec1 = Record("John")
rec1.add_phone("1234567890")
rec1.add_phone("5555555555")
book.add_record(rec1)
rec2 = Record("Jane")
rec2.add_phone("4444444444")
book.add_record(rec2)

print(book)
