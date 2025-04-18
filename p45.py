# Write a Python program to create a person class.
# Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (
                today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}"


# Example usage:
person = Person("John Doe", "USA", "1990-05-15")
print(person)  # Print person details
print(f"Age: {person.get_age()}")  # Print person's age
