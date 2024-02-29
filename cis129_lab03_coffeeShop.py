# Author: Wolfgang C. Stover
#CIS 129
# Program: Coffee Shop Simulator
# Description: This program simulates a coffee shop by calculating the receipt based on the number of items ordered.

# Function to calculate the receipt based on user input
def calculate_receipt(coffees, muffins):
    # Price of coffee and muffin
    coffee_price = 5
    muffin_price = 4
    
    # Calculate subtotal
    subtotal = (coffees * coffee_price) + (muffins * muffin_price)
    
    # Calculate tax (6%)
    tax = subtotal * 0.06
    
    # Calculate total
    total = subtotal + tax
    
    # Display receipt
    print("***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{coffees} Coffee at ${coffee_price} each: ${coffees * coffee_price:.2f}")
    print(f"{muffins} Muffins at ${muffin_price} each: ${muffins * muffin_price:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("***************************************")

# Main function
def main():
    # Welcome message
    print("*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@")
    print("Welcome to My Coffee and Muffin Shop")
    print("*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@*@‽*@‽*@")
    
    # Get user input
    coffees = int(input("Number of coffees bought?"))
    muffins = int(input("Number of muffins bought?"))
    
    # Calculate and display receipt
    calculate_receipt(coffees, muffins)
    
    # Thank you message
    print("Thank you for visiting My Coffee and Muffin Shop! We hope to see you again soon.")
