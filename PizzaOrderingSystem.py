import tkinter as tk
from tkinter import messagebox

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Food Ordering System")

        # Menu Bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Login", command=self.show_login_window)
        file_menu.add_command(label="Exit", command=root.destroy)
        menubar.add_cascade(label="File", menu=file_menu)

        # Initialize login window
        self.login_window = LoginWindow(root)

    def show_login_window(self):
        self.login_window.show()

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        # Login components (labels, entry, button)
        tk.Label(self.master, text="Username:").pack(pady=10)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)

        tk.Label(self.master, text="Password:").pack(pady=10)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.master, text="Login", command=self.login).pack(pady=10)

    def login(self):
        # Placeholder for login logic
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace this with your actual login validation logic
        if username == "user" and password == "pass":
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
            # Placeholder for opening the home page window
            self.master.withdraw()
            home_window = HomePageWindow(self.master)
            home_window.show()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show(self):
        self.master.deiconify()

class HomePageWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Home Page")
        self.master.geometry("600x400")

        # Placeholder for home page components (menu, cart, etc.)
        tk.Label(self.master, text="Welcome to the Home Page").pack(pady=20)

        # Placeholder for menu items
        menu_items = [
            {"name": "Item 1", "price": 10.99},
            {"name": "Item 2", "price": 5.99},
            {"name": "Item 3", "price": 8.49},
        ]

        # Display menu items
        for item in menu_items:
            tk.Label(self.master, text=f"{item['name']}: ${item['price']:.2f}").pack()

        # Cart components
        self.cart = []  # List to store selected items

        def add_to_cart(item):
            self.cart.append(item)
            messagebox.showinfo("Cart", f"{item['name']} added to cart!")

        # Add buttons for each menu item to add to the cart
        for item in menu_items:
            add_button = tk.Button(self.master, text=f"Add to Cart ({item['name']})", command=lambda i=item: add_to_cart(i))
            add_button.pack(pady=5)

        # Display cart
        tk.Label(self.master, text="Cart:").pack()
        for cart_item in self.cart:
            tk.Label(self.master, text=f"{cart_item['name']}").pack()

        # Clear cart button
        tk.Button(self.master, text="Clear Cart", command=self.clear_cart).pack(pady=10)

        # Proceed to Payment button
        tk.Button(self.master, text="Proceed to Payment", command=self.show_payment_window).pack(pady=10)

    def clear_cart(self):
        self.cart.clear()
        messagebox.showinfo("Cart Cleared", "Your cart has been cleared!")

    def show_payment_window(self):
        # Placeholder for opening the payment window
        self.master.withdraw()
        payment_window = PaymentWindow(self.master, self.cart)
        payment_window.show()

    def show(self):
        self.master.deiconify()

class PaymentWindow:
    def __init__(self, master, cart):
        self.master = master
        self.master.title("Payment")
        self.master.geometry("400x300")

        # Placeholder for payment components (payment form, etc.)
        tk.Label(self.master, text="Enter Payment Information").pack(pady=20)

        # Display cart items
        tk.Label(self.master, text="Cart:").pack()
        for cart_item in cart:
            tk.Label(self.master, text=f"{cart_item['name']}").pack()

        # Payment form components
        tk.Label(self.master, text="Card Number:").pack(pady=5)
        self.card_entry = tk.Entry(self.master)
        self.card_entry.pack(pady=5)

        tk.Label(self.master, text="Expiry Date:").pack(pady=5)
        self.expiry_entry = tk.Entry(self.master)
        self.expiry_entry.pack(pady=5)

        tk.Label(self.master, text="CVV:").pack(pady=5)
        self.cvv_entry = tk.Entry(self.master, show="*")
        self.cvv_entry.pack(pady=5)

        tk.Button(self.master, text="Place Order", command=lambda: self.show_confirmation_window(cart)).pack(pady=10)

    def show_confirmation_window(self, cart):
        # Placeholder for opening the confirmation window
        self.master.withdraw()
        confirmation_window = ConfirmationWindow(self.master, self.card_entry.get(), self.expiry_entry.get(), self.cvv_entry.get(), cart)
        confirmation_window.show()

    def show(self):
        self.master.deiconify()

class ConfirmationWindow:
    def __init__(self, master, card_number, expiry_date, cvv, cart):
        self.master = master
        self.master.title("Order Confirmation")
        self.master.geometry("500x400")

        # Placeholder for confirmation components (order summary, etc.)
        tk.Label(self.master, text="Order Summary").pack(pady=20)

        # Display payment information
        tk.Label(self.master, text=f"Card Number: {card_number}").pack()
        tk.Label(self.master, text=f"Expiry Date: {expiry_date}").pack()
        tk.Label(self.master, text=f"CVV: {cvv}").pack()

        # Display order summary
        tk.Label(self.master, text="Items Purchased:").pack()
        for cart_item in cart:
            tk.Label(self.master, text=f"{cart_item['name']}").pack()

        tk.Button(self.master, text="Finish", command=self.finish_order).pack(pady=10)

    def finish_order(self):
        # Placeholder for order completion logic
        messagebox.showinfo("Order Placed", "Thank you for your order!")
        self.master.destroy()

    def show(self):
        self.master.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
