import tkinter as tk
from tkinter import ttk, messagebox

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Food Ordering System")

        # Modern Theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

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

class ThemedMixin:
    def __init__(self, master):
        self.master = master
        self.style = ttk.Style()

class LoginWindow(ThemedMixin):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Login")
        self.master.geometry("300x200")

        # Login components (labels, entry, button)
        self.frame = ttk.Frame(self.master)
        self.frame.pack(pady=20)

        ttk.Label(self.frame, text="Username:").grid(row=0, column=0, pady=10, padx=10, sticky="e")
        self.username_entry = ttk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(self.frame, text="Password:").grid(row=1, column=0, pady=10, padx=10, sticky="e")
        self.password_entry = ttk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5, padx=10)

        ttk.Button(self.master, text="Login", command=self.login).pack(pady=10)

    def login(self):
        # Placeholder for login logic
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace this with your actual login validation logic
        if username == "user" and password == "pass":
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            # Placeholder for opening the home page window
            self.master.withdraw()
            home_window = HomePageWindow(self.master)
            home_window.show()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show(self):
        self.master.deiconify()

class HomePageWindow(ThemedMixin):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Home Page")
        self.master.geometry("600x400")

        # Placeholder for home page components (menu, cart, etc.)
        ttk.Label(self.master, text="Welcome to the Home Page").pack(pady=20)

        self.menu_frame = ttk.Frame(self.master)
        self.menu_frame.pack(pady=10)

        # Placeholder for menu items
        menu_items = [
            {"name": "Deluxe Pizza", "price": 10.99},
            {"name": "Cheese Pizza", "price": 5.99},
            {"name": "Pepperoni Pizza", "price": 8.49},
        ]

        # Display menu items
        for item in menu_items:
            ttk.Label(self.menu_frame, text=f"{item['name']}: ${item['price']:.2f}").pack()

        self.cart_frame = ttk.Frame(self.master)
        self.cart_frame.pack(pady=10)

        # Cart components
        self.cart = []  # List to store selected items

        # Listbox to display cart items
        self.cart_listbox = tk.Listbox(self.cart_frame)
        self.cart_listbox.pack()

        def add_to_cart(item):
            self.cart.append(item)
            self.cart_listbox.insert(tk.END, f"{item['name']} - ${item['price']:.2f}")
            messagebox.showinfo("Cart", f"{item['name']} added to cart!")

        # Add buttons for each menu item to add to the cart
        for item in menu_items:
            ttk.Button(self.menu_frame, text=f"Add to Cart ({item['name']})", command=lambda i=item: add_to_cart(i)).pack(pady=5)

        # Clear cart button
        ttk.Button(self.cart_frame, text="Clear Cart", command=self.clear_cart).pack(pady=10)

        # Proceed to Payment button
        ttk.Button(self.cart_frame, text="Proceed to Payment", command=self.show_payment_window).pack(pady=10)

    def clear_cart(self):
        self.cart.clear()
        self.cart_listbox.delete(0, tk.END)  # Clear the Listbox
        messagebox.showinfo("Cart Cleared", "Your cart has been cleared!")

    def show_payment_window(self):
        # Placeholder for opening the payment window
        PaymentWindow(self.master, self.cart)

    def show(self):
        self.master.deiconify()

class PaymentWindow(tk.Toplevel, ThemedMixin):
    def __init__(self, master, cart):
        super().__init__(master)
        self.title("Payment")
        self.geometry("400x300")

        # Placeholder for payment components (payment form, etc.)
        ttk.Label(self, text="Enter Payment Information").pack(pady=20)

        # Display cart items
        ttk.Label(self, text="Cart:").pack()
        for cart_item in cart:
            ttk.Label(self, text=f"{cart_item['name']}").pack()

        # Payment form components
        ttk.Label(self, text="Card Number:").pack(pady=5)
        self.card_entry = ttk.Entry(self)
        self.card_entry.pack(pady=5)

        ttk.Label(self, text="Expiry Date:").pack(pady=5)
        self.expiry_entry = ttk.Entry(self)
        self.expiry_entry.pack(pady=5)

        ttk.Label(self, text="CVV:").pack(pady=5)
        self.cvv_entry = ttk.Entry(self, show="*")
        self.cvv_entry.pack(pady=5)

        ttk.Button(self, text="Place Order", command=lambda: self.show_confirmation_window(cart)).pack(pady=10)
        
        # Go Back button
        ttk.Button(self, text="Go Back", command=self.go_back).pack(pady=10)

    def show_confirmation_window(self, cart):
        # Placeholder for opening the confirmation window
        confirmation_window = ConfirmationWindow(self.master, self.card_entry.get(), self.expiry_entry.get(), self.cvv_entry.get(), cart)
        confirmation_window.protocol("WM_DELETE_WINDOW", lambda: self.on_confirmation_window_close(confirmation_window))
        confirmation_window.grab_set()

    def go_back(self):
        # Close the current payment window and show the home page window
        self.destroy()
        self.master.deiconify()

def on_confirmation_window_close(self, confirmation_window):
    self.destroy()
    confirmation_window.destroy()


class ConfirmationWindow(tk.Toplevel, ThemedMixin):
    def __init__(self, master, card_number, expiry_date, cvv, cart):
        super().__init__(master)
        self.title("Order Confirmation")
        self.geometry("500x400")

        # Placeholder for confirmation components (order summary, etc.)
        ttk.Label(self, text="Order Summary").pack(pady=20)

        # Display payment information
        ttk.Label(self, text=f"Card Number: {card_number}").pack()
        ttk.Label(self, text=f"Expiry Date: {expiry_date}").pack()
        ttk.Label(self, text=f"CVV: {cvv}").pack()

        # Display order summary
        ttk.Label(self, text="Items Purchased:").pack()
        for cart_item in cart:
            ttk.Label(self, text=f"{cart_item['name']}").pack()

        ttk.Button(self, text="Finish", command=self.finish_order).pack(pady=10)

    def finish_order(self):
    # Placeholder for order completion logic
        messagebox.showinfo("Order Placed", "Thank you for your order!")
        self.master.destroy()
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)

    # Load and add images
    try:
        pizza_image = tk.PhotoImage(file=r"C:\Users\Nikoli\Desktop\Final Pizza\pizza_image.png")
        logo_image = tk.PhotoImage(file=r"C:\Users\Nikoli\Desktop\Final Pizza\logo_image.png")
    except tk.TclError as e:
        print(f"Error loading images: {e}")

    if 'pizza_image' in locals() and pizza_image:
        ttk.Label(root, image=pizza_image).pack(pady=10)
    if 'logo_image' in locals() and logo_image:
        ttk.Label(root, image=logo_image).pack(pady=10)

    root.mainloop()



