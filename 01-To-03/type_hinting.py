from typing import Any

# by default variable types are dynamic in python

text = "abid"
print(text)
text = 10
print(text)

# by hinting type, the methods are displayed by the IDE then
name: str = "abid"
print(name.upper())

name = True
print(name)

# Opitonal, either None or a String
fianceName: str | None = None

print(fianceName)



def table( num: int, to: int | None = 10):
    counter: int = 1
    while counter <= to:
        print(f"{num} X {counter} = {num*counter} ")
        counter += 1

# table(num=5)
# print('*****************************')
# table(num=7, to=20)

shopping_list: list[str] = ['apple', 'mango', 'milk', 'bread']
price_list: list[float] = [60.6, 54.4, 300, 180]

for item in zip(shopping_list, price_list):
    print(item[0], item[1])

print(type(shopping_list))

user: dict[str, Any] = {
    "id": 1,
    "name": "Ali",
    "cgpa": 3.4,
    "is_married": False
}

print(user)
print(type(user))

class Address:
    def __init__(self, street_no: str, city: str, country: str):
        self.street_no = street_no
        self.city = city
        self.country = country

address1 = Address(street_no="Street No 5", city="Peshawar", country="Pakistan")

class Student:
    def __init__(self, name, course, mobile, address: Address | None = None):
        self.name = name
        self.course = course
        self.mobile = mobile
        self.address = address

    def display(self):
        addr = f"{self.address.street_no}-{self.address.city}-{self.address.country}" if self.address is not None else "Not Given"
        info: str = f"""
        Name: {self.name}
        Course: {self.course}
        Mobile: {self.mobile}
        Address: {addr}
        """
        print(info)

ali = Student(name="Abid", course="AI Agentic", mobile="03329964494", address=address1)
ali.display()