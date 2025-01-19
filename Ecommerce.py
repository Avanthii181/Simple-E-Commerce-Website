import tkinter as tk
from tkinter import messagebox

# Product list (dummy data)
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Smartphone', 'price': 700},
    {'id': 3, 'name': 'Headphones', 'price': 200},
]

# Initialize cart
cart = []

# Function to add product to the cart
def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Cart", f"{product['name']} added to cart!")

# Function to view cart
def view_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Shopping Cart")

    if cart:
        tk.Label(cart_window, text="Your Cart", font=("Arial", 16)).pack(pady=10)

        total_price = 0
        for product in cart:
            tk.Label(cart_window, text=f"{product['name']} - ${product['price']}").pack()
            total_price += product['price']

        tk.Label(cart_window, text=f"Total: ${total_price}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Button(cart_window, text="Checkout", command=checkout).pack(pady=5)
    else:
        tk.Label(cart_window, text="Your cart is empty.", font=("Arial", 14)).pack(pady=10)

# Function to handle checkout
def checkout():
    if cart:
        cart.clear()
        messagebox.showinfo("Order", "Order placed successfully!")
    else:
        messagebox.showwarning("Order", "Your cart is empty!")

# Initialize the main window
root = tk.Tk()
root.title("E-commerce Application")
root.geometry("400x300")

# Header
tk.Label(root, text="Welcome to the E-commerce Store", font=("Arial", 16, "bold")).pack(pady=10)

# Product List
for product in PRODUCTS:
    frame = tk.Frame(root)
    frame.pack(pady=5)

    tk.Label(frame, text=f"{product['name']} - ${product['price']}", font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
    tk.Button(frame, text="Add to Cart", command=lambda p=product: add_to_cart(p)).pack(side=tk.RIGHT)

# View Cart Button
tk.Button(root, text="View Cart", command=view_cart, font=("Arial", 12)).pack(pady=20)

# Start the application
root.mainloop()
