# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = []  # List to store items in the cart

    def add_item(self, item_name, price):
        """Add an item to the shopping cart."""
        self.items.append({"name": item_name, "price": price})

    def remove_item(self, item_name):
        """Remove an item from the shopping cart by name."""
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                return
        print(f"{item_name} not found in cart.")

    def calculate_total(self):
        """Calculate the total price of all items in the cart."""
        total = sum(item['price'] for item in self.items)
        return total


# Example usage:
cart = ShoppingCart()

# Adding items
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 25)

# Calculating total
print(f"Total price: ${cart.calculate_total()}")

# Removing an item
cart.remove_item("Mouse")

# Calculating total after removal
print(f"Total price after removal: ${cart.calculate_total()}")
