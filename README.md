from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter
from tkinter import BooleanVar
from tkinter import messagebox
import time

# Price dictionary for all items
PRICES = {
    "burgers": {
        "Classic Burger": 120,
        "Veggie Burger": 130,
        "Cheesy Burger": 140,
        "Cheesy Bacon Burger": 150,
        "Ultimate Burger": 160,
    },
    "fries": {
        "Small Fries": 47,
        "Medium Fries": 65,
        "Large Fries": 80,
    },
    "drinks": {
        "Coffee": 50,
        "Hot Choco": 60,
        "Iced Tea": 40,
        "Juice": 45,
        "Soft Drinks": 35,
    },
    "pizza": {
        "Ham and Cheese Pizza": 200,
        "Pepperoni Pizza": 220,
        "Hawaiian Pizza": 210,
        "Cheese Pizza": 190,
        "Veggie Pizza": 230,
    }
}

# Main Display
dash_board = tk.Tk()
dash_board.title('Shop Dash Board')
dash_board.geometry("1200x600")
dash_board.configure(bg='white')
dash_board.resizable(False, False)

# Set the icon for the window
icon = PhotoImage(file='icon.png')
dash_board.iconphoto(True, icon)

# Function to load and resize images
def load_image(path, size):
    try:
        image = Image.open(path)
        image = image.resize(size)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image {path}: {e}")
        return None

# Background
background_image_tk = load_image("Background.png", (1200, 600))
if background_image_tk:
    background_label = Label(dash_board, image=background_image_tk)
    background_label.place(relx=0.5, rely=0.5, anchor="center")

# Logo
logo_image_tk = load_image("Logo.png", (60, 60))
if logo_image_tk:
    logo_label = Label(dash_board, image=logo_image_tk, bg='white')
    logo_label.place(x=100, y=50)

# Search Icon
search_image_tk = load_image("search.png", (40, 40))
if search_image_tk:
    search_image = Label(dash_board, image=search_image_tk, bg='white')
    search_image.place(x=170, y=55)

# Placeholder Text
place_holder_text = "Search here"

# Function to handle when the user clicks inside the entry
def on_click(event):
    if search.get() == place_holder_text:
        search.delete(0, tk.END)  # Clear the placeholder text when clicked
        search.config(fg='black')  # Change text color to black

# Function to handle when the user clicks outside the entry
def off_click(event):
    if search.get() == "":
        search.insert(0, place_holder_text)  # Insert the placeholder text if nothing is typed
        search.config(fg='gray')  # Change text color back to gray

# Search Entry Widget
search = Entry(dash_board, bd=0, width=65, highlightthickness=0,fg='gray', font=('Arial', 12))
search.insert(0, place_holder_text)  # Insert placeholder text initially
search.place(x=210, y=67)

# Bind the events for click and focus out
search.bind("<FocusIn>", on_click)  # When the user clicks inside
search.bind("<FocusOut>", off_click)  # When the user clicks outside

# Function to search and display relevant items
def search_items(event=None):
    query = search.get().strip().lower()  # Get user input and convert to lowercase for consistency
    if query == "burger":
        display_burgers()
    elif query == "fries":
        display_fries()
    elif query == "pizza":
        display_pizzas()
    elif query == "drinks":
        display_drinks()
    elif query == place_holder_text.lower():  # Ignore the placeholder text
        print("Please enter a search term.")
    else:
        print(f"No items found for '{query}'. Showing Home.")
        display_home()

# Bind the search entry widget to the Enter key
search.bind("<Return>", search_items)

def show_frame(frame):
    # Hide all other frames
    for f in [scrollable_frame_home, scrollable_frame_pizza, scrollable_frame_burger,
              scrollable_frame_fries, scrollable_frame_drinks]:
        f.place_forget()
    # Show the selected frame
    frame.place(x=180, y=120)

# Function to clear the scrollable frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Scrollable Frames for items
scrollable_frame_home = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_pizza = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_burger = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_fries = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_drinks = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_home.place(x=180, y=120)

# Global variables
selected_items_panel = None
sub_total = None
delivery_charge = None
total = None
Orders = None
place_order = None
max_attempt = 3
incorrect_attempts = 0
ads_label = None
login_frame = None
receipt_text_widget = None


# Display ads
def ads():
    global ads_label, ads_image_tk
    ads_image_tk = load_image("ads.png", (270, 390))
    if ads_image_tk:
        ads_label = Label(dash_board, image=ads_image_tk, bg='white')
        ads_label.place(x=820, y=120)

# Function to hide the receipt frame
def hide_receipt_frame():
    global receipt_text_widget, place_order

    # Destroy the receipt text widget if it exists
    if receipt_text_widget:
        receipt_text_widget.destroy()
        receipt_text_widget = None

    # Destroy the "Place Another Order" button if it exists
    if place_order:
        place_order.destroy()
        place_order = None

# Display Chosen Items Function
def display_chosen_items():
    global selected_items_panel, sub_total, delivery_charge, total, Orders, place_order

    # Scrollable Frame for chosen items
    selected_items_panel = customtkinter.CTkScrollableFrame(dash_board, width=250, height=1)
    selected_items_panel.place(x=820, y=120)

    Orders = ttk.Label(dash_board, text="Orders:", foreground='white', background='#DB7921',
                       font=("Helvetica", 18, 'bold'))
    Orders.place(x=820, y=80)

    # Divider
    divider = tk.Canvas(dash_board, background="light gray", height=1, width=220)
    divider.place(x=850, y=400)

    # Labels for totals
    sub_total = ttk.Label(dash_board, text="Sub Total:                      ₱0.00", foreground="gray",
                          font=("Arial", 12))
    sub_total.place(x=860, y=340)

    delivery_charge = ttk.Label(dash_board, text="Delivery Charges:         ₱0.00", foreground="gray",
                                font=("Arial", 12))
    delivery_charge.place(x=860, y=370)

    total = ttk.Label(dash_board, text="Total:                              ₱0.00", foreground="gray",
                      font=("Arial", 12))
    total.place(x=860, y=420)

    # Place Order Button
    place_order = Button(
        dash_board,
        width=20,
        height=2,
        text='Place Order',
        bg='#DB7921',
        foreground='white',
        font=('Arial', 15, 'bold'),
        border=0
    )
    place_order.place(x=840, y=460)

# Dictionary to track selected items and their quantities
selected_items = {}

# Fix: Update the selected items dynamically when added or removed
def refresh_selected_items():
    global selected_items_panel

    # Clear the current display in the selected items panel
    for widget in selected_items_panel.winfo_children():
        widget.destroy()

    # Add all selected items to the display
    for idx, (item_name, item_data) in enumerate(selected_items.items()):
        item_frame = Frame(selected_items_panel, bg='white', bd=2, relief="groove")
        item_frame.grid(row=idx, column=0, sticky="ew", padx=5, pady=5)

        # Label to show the item name, quantity, and total price
        item_label = Label(
            item_frame,
            text=f"{item_name} x{item_data['quantity']} - ₱{item_data['quantity'] * item_data['price']:.2f}",
            font=("Arial", 8),
            bg="white",
        )
        item_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Remove button to decrease the quantity or remove the item
        remove_button = Button(
            item_frame,
            text="Remove",
            font=("Arial", 8),
            fg="red",
            bg="white",
            relief="flat",
            command=lambda item=item_name: remove_from_selected_items(item)
        )
        remove_button.grid(row=0, column=1, padx=10, pady=5, sticky="e")

    # Update the totals after refreshing the selected items
    update_totals()

def add_to_selected_items(item_name, item_price):
    global selected_items_panel

    if item_name in selected_items:
        selected_items[item_name]['quantity'] += 1
    else:
        selected_items[item_name] = {'price': item_price, 'quantity': 1}

    refresh_selected_items()  # Refresh after adding

def remove_from_selected_items(item_name):
    global selected_items_panel

    if item_name in selected_items:
        selected_items[item_name]['quantity'] -= 1
        if selected_items[item_name]['quantity'] <= 0:
            del selected_items[item_name]
        refresh_selected_items()  # Refresh after removal
    else:
        print(f"Item '{item_name}' not found.")  # Debug


# Fix: Update totals based on selected items
def update_totals():
    global selected_items_panel

    subtotal = sum(data['price'] * data['quantity'] for data in selected_items.values())
    delivery_fee = 50 if subtotal > 0 else 0  # Example delivery charge logic
    total_amount = subtotal + delivery_fee

    # Update labels to reflect the current totals
    sub_total.config(text=f"Sub Total: ₱{subtotal:.2f}")
    delivery_charge.config(text=f"Delivery Charges: ₱{delivery_fee:.2f}")
    total.config(text=f"Total: ₱{total_amount:.2f}")

    # Place Order Button to trigger the print_receipt function
    place_order = Button(
        dash_board,
        width=20,
        height=2,
        text='Place Order',
        bg='#DB7921',
        foreground='white',
        font=('Arial', 15, 'bold'),
        border=0,
        command=lambda: print_receipt(selected_items, receipt_text_widget)  # Pass the Text widget here
    )
    place_order.place(x=840, y=460)

# Function to create a button with an image and text for two columns in a scrollable frame
def home_button(parent, image_path, button_text, row, column):
    try:
        icon_photo = PhotoImage(file=image_path)
        icon_photo_resized = icon_photo.subsample(3, 3)

        # Parse item details from button text
        text_split = button_text.split(":")
        item_name = text_split[1].strip()
        item_price = float(text_split[0][1:].strip())

        button = Button(
            parent,
            text=button_text,
            fg='gray',
            font=('Arial', 8),
            image=icon_photo_resized,
            compound='top',
            bg=dash_board.cget('bg'),
            activebackground=dash_board.cget('bg'),
            relief="flat",
            command=lambda: add_to_selected_items(item_name, item_price)
        )
        button.image = icon_photo_resized
        button.grid(row=row, column=column, padx=10, pady=10)
    except Exception as e:
        print(f"Error creating button {button_text}: {e}")

# Function to display the home buttons in two columns
def display_home():
    clear_frame(scrollable_frame_home)
    buttons = [
        ('classic.png', '₱85: Classic Burger'),
        ('medium.png', '₱65: Medium Fries'),
        ('_Ham and Cheese.png', '₱120: Ham & Cheese Pizza'),
        ('cheese pizza.png', '₱115: Cheese Pizza'),
        ('iced tea.png', '₱45: Iced Tea'),
        ('ultimate.png', '₱150: Ultimate Burger'),
        ('cheese.png', '₱95: Cheesy Burger'),
        ('soft drinks.png', '₱40: Soft Drinks'),
        ('pepperoni.png', '₱140: Pepperoni Pizza'),
        ('Hawaiian (1).png', '₱130: Hawaiian Pizza'),
        ('hot choco.png', '₱55: Hot Choco'),
        ('veggie.png', '₱90: Veggie Burger'),
        ('small.png', '₱47: Small Fries'),
        ('coffee.png', '₱50: Coffee'),
        ('juice.png', '₱60: Juice')
    ]

    row, column = 0, 0
    for image, text in buttons:
        home_button(scrollable_frame_home, image, text, row, column)
        column += 1
        if column > 2:  # After 3 columns, reset to column 0 and go to the next row
            column = 0
            row += 1

    # Ensure the home frame is displayed and others are hidden
    show_frame(scrollable_frame_home)

def display_pizzas():
    clear_frame(scrollable_frame_home)

    # Button placement logic: Column 0 and 1, after every 2 buttons move to next row.
    buttons = [
        ('_Ham and Cheese.png', '₱120: Ham and Cheese Pizza'),
        ('pepperoni.png', '₱140: Pepperoni Pizza'),
        ('Hawaiian (1).png', '₱130: Hawaiian Pizza'),
        ('cheese pizza.png', '₱115: Cheese Pizza'),
        ('Veggie pizza.png', '₱125: Veggie Pizza')
    ]

    row, column = 0, 0
    for image, text in buttons:
        home_button(scrollable_frame_home, image, text, row, column)
        column += 1
        if column > 2:  # After 3 columns, reset to column 0 and go to the next row
            column = 0
            row += 1

def display_burgers():
    clear_frame(scrollable_frame_home)

    # Button placement logic: Column 0 and 1, after every 2 buttons move to next row.
    buttons = [
        ('classic.png', '₱85: Classic Burger'),
        ('veggie.png', '₱90: Veggie Burger'),
        ('cheese.png', '₱95: Cheesy Burger'),
        ('cheesy bacon.png', '₱120: Cheesy Bacon Burger'),
        ('ultimate.png', '₱150: Ultimate Burger')
    ]

    row, column = 0, 0
    for image, text in buttons:
        home_button(scrollable_frame_home, image, text, row, column)
        column += 1
        if column > 2:  # After 3 columns, reset to column 0 and go to the next row
            column = 0
            row += 1

def display_fries():
    clear_frame(scrollable_frame_home)

    # Button placement logic: Column 0, 1, 2, after every 3 buttons move to the next row.
    buttons = [
        ('small.png', '₱47: Small Fries'),
        ('medium.png', '₱65: Medium Fries'),
        ('large.png', '₱80: Large Fries')
    ]

    row, column = 0, 0
    for image, text in buttons:
        home_button(scrollable_frame_home, image, text, row, column)
        column += 1
        if column > 2:  # After 3 columns, reset to column 0 and go to the next row
            column = 0
            row += 1

def display_drinks():
    clear_frame(scrollable_frame_home)

    # Button placement logic: Column 0 and 1, after every 2 buttons move to next row.
    buttons = [
        ('coffee.png', '₱50: Coffee'),
        ('hot choco.png', '₱55: Hot Choco'),
        ('iced tea.png', '₱45: Iced Tea'),
        ('juice.png', '₱60: Juice'),
        ('soft drinks.png', '₱40: Soft Drinks'),
        ('milk shake.png', '₱70: Milk Shake')
    ]

    row, column = 0, 0
    for image, text in buttons:
        home_button(scrollable_frame_home, image, text, row, column)
        column += 1
        if column > 2:  # After 3 columns, reset to column 0 and go to the next row
            column = 0
            row += 1

# Variable to track the active button
active_button = None

def update_button_color(button):
    global active_button

    # Reset the previous button's background color
    if active_button:
        active_button.config(bg=dash_board.cget('bg'))  # Reset to default background

    # Set the clicked button as active and change its background color
    button.config(bg='#D3D3D3')  # Slightly dark gray for active state
    active_button = button

# Create Buttons for navigation between different categories
def create_button(image_path, button_text, x, y, command=None):
    try:
        icon_photo = PhotoImage(file=image_path)
        icon_photo_resized = icon_photo.subsample(12, 12)
        button = Button(
            dash_board,
            text=button_text,
            fg='gray',
            font=('Arial', 8),
            image=icon_photo_resized,
            compound='top',
            bg=dash_board.cget('bg'),
            activebackground=dash_board.cget('bg'),
            relief="flat",
            command=command
        )
        button.image = icon_photo_resized
        button.place(x=x, y=y)
    except Exception as e:
        print(f"Error creating button {button_text}: {e}")


# Function to hide the chosen items section and ads
def hide_display_chosen_items():
    global selected_items_panel, sub_total, delivery_charge, total, Orders, place_order

    if selected_items_panel:
        Orders.place_forget()  # Hide the Orders label
        selected_items_panel.place_forget()  # Hide the selected items panel
        sub_total.place_forget()  # Hide the Sub Total label
        delivery_charge.place_forget()  # Hide the Delivery Charges label
        total.place_forget()  # Hide the Total label
        place_order.place_forget()  # Hide The Place Order Button

def hide_ads():
    global ads_label
    if ads_label:
        ads_label.destroy()  # Remove the ads widget
        ads_label = None  # Reset the reference

# Accounts data: username -> (password, role)
accounts = {
    "admin": ("1234", "admin"),
    "staff": ("5678", "staff")
}

# Function to update password visibility based on checkbox
def toggle_password_visibility(password_entry, show_password_var):
    if show_password_var.get():
        password_entry.config(show='')  # Show password (text input)
    else:
        password_entry.config(show='*')  # Hide password (show '*' characters)

# Function to disable login form
def disable_form():
    username.config(state=DISABLED)
    password.config(state=DISABLED)
    sign_in_button.config(state=DISABLED)
    forgot_password_button.config(state=DISABLED)
    show_password_checkbox.config(state=DISABLED)
    messagebox.showerror("Too Many Attempts", "You have reached the maximum number of login attempts. Please try again later.")

# Function to display staff dashboard (stub for now)
def display_admin_dashboard():
    messagebox.showinfo("Login Successful", "Welcome, Admin!")
    # Add functionality for staff dashboard here

def staff():
    login_button.config(state=DISABLED)
    display_chosen_items()

# Function to validate login credentials
def validate_login():
    global incorrect_attempts
    user_input = username.get()
    pass_input = password.get()

    if user_input in accounts:
        account_password, role = accounts[user_input]
        if pass_input == account_password:
            login_frame.destroy()
            if role == "admin":
                display_admin_dashboard()  # Admin dashboard
            elif role == "staff":
                  staff() # Staff dashboard

            return
        else:
            messagebox.showerror('Invalid', "Incorrect password")
    else:
        messagebox.showerror('Invalid', "Invalid username")

    # Increment incorrect attempts for invalid credentials
    incorrect_attempts += 1

    if incorrect_attempts >= max_attempt:
        disable_form()

def forgot_password():
    # Password Recovery Form
    password_recovery_window = Tk()
    password_recovery_window.title('Password Retrieval')
    password_recovery_window.geometry("925x500+300+200")
    password_recovery_window.configure(bg='white')
    password_recovery_window.resizable(False, False)

    frame = Frame(password_recovery_window, width=350, height=350, bg='white', relief=RAISED, bd=5)
    frame.place(x=280, y=70)

    heading = Label(frame, text='Password Recovery', fg='white', bg='#DB7921', font=('Arial', 20, 'bold'))
    heading.place(x=25, y=10)

    # Email Textbox
    user = Entry(frame, width=35, font=('Arial', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Email')

    # Line under email
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # Password Textbox
    password = Entry(frame, width=35, bg='white', font=('Arial', 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')

    # Line under password
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    max_attempt = 3
    incorrect_attempts = 0

    # Function for focus in and out (Textbox behavior)
    def on_enter_user(e):
        user.delete(0, 'end')

    def on_leave_user(e):
        if user.get() == '':
            user.insert(0, 'Email')

    user.bind('<FocusIn>', on_enter_user)
    user.bind('<FocusOut>', on_leave_user)

    def on_enter_pass(e):
        if password.get() == 'Password':
            password.delete(0, 'end')
        password.config(show="*")

    def on_leave_pass(e):
        if password.get() == '':
            password.insert(0, 'Password')
        else:
            password.config(show="*")

    password.bind('<FocusIn>', on_enter_pass)
    password.bind('<FocusOut>', on_leave_pass)

    # Function to Disable Form
    def disable_form():
        user.config(state=DISABLED)
        password.config(state=DISABLED)
        submit.config(state=DISABLED)

        messagebox.showerror("Too Many Attempts", "You have reached the maximum number of login attempts. Please try again later.")

    # Submit Button Command
    def submit():
        global incorrect_attempts

        if incorrect_attempts >= max_attempt:
            disable_form()
            return

        username = user.get()
        password1 = password.get()

        # Dummy password check for now
        if username == 'admin@rtu.com' and password1 == '1234':
            messagebox.showinfo("Password Recovery", f"Hi! {username} Your password: {password1}")
            password_recovery_window.destroy()

        else:
            messagebox.showerror('Invalid', "Invalid username or password")
            incorrect_attempts += 1

        if incorrect_attempts == max_attempt:
            disable_form()

    # Submit Button
    Button(frame, width=39, pady=10, text='Submit', bg='#DB7921', fg='white', command=submit, border=0).place(x=35, y=210)


# Function to display login form
def login_display():
    global username, password, sign_in_button, forgot_password_button, show_password_checkbox, login_frame
    hide_ads()
    login_frame = Frame(dash_board, width=270, height=390, bg='light gray', bd=5)
    login_frame.place(x=820, y=120)

    heading = Label(login_frame, text='Log In', fg='#DB7921', bg='light gray', font=('Roboto', 24, 'bold'))
    heading.place(x=75, y=10)

    # Username Textbox
    tk.Label(login_frame, text="Username:", font=('Arial', 14), fg='gray', bg='light gray').place(x=10, y=100)
    username = Entry(login_frame, bd=0, width=20, highlightthickness=0, fg='gray', font=('Arial', 14))
    username.place(x=10, y=130)

    # Password Textbox
    tk.Label(login_frame, text="Password:", font=('Arial', 14), fg='gray', bg='light gray').place(x=10, y=160)
    password = Entry(login_frame, bd=0, width=20, highlightthickness=0, fg='gray', font=('Arial', 14), show="*")
    password.place(x=10, y=190)

    # BooleanVar to track the checkbox state
    show_password_var = BooleanVar()

    # Show Password Checkbox
    show_password_checkbox = Checkbutton(
        login_frame,
        text="Show Password",
        bg='light gray',
        fg='#DB7921',
        font=('Arial', 8),
        variable=show_password_var,
        command=lambda: toggle_password_visibility(password, show_password_var)
    )
    show_password_checkbox.place(x=10, y=214)

    # Forgot Password Button
    forgot_password_button = Button(login_frame,command=forgot_password,width=20, text='Forgot Password?', border=0, bg='light gray',font=('Arial', 8), cursor='hand2', fg='#DB7921')
    forgot_password_button.place(x=120, y=216)

    # Sign In Button
    sign_in_button = Button(login_frame, width=33, pady=10, text='Sign in', bg='#DB7921', fg='white', border=0,command=validate_login)
    sign_in_button.place(x=10, y=250)


# Login Button
login_image_tk = load_image("Login.png", (40, 40))
if login_image_tk:
    login_button = Button(dash_board,relief="flat", image=login_image_tk,fg='gray',bg='white', text='Login', compound="top", command=login_display)
    login_button.place(x=100, y=120)

#Create the buttons using the function
create_button('home.png', 'Home', 100, 180, command=display_home)
create_button('pizza.png', 'Pizza', 100, 240, command=display_pizzas)
create_button('burger.png', 'Burger', 100, 300, command=display_burgers)
create_button('fries.png', 'Fries', 100, 360, command=display_fries)
create_button('drinks.png', 'Drinks', 100, 420, command=display_drinks)

# Footer
Footer = ttk.Label(dash_board, text="© 2024 | Icons, backgrounds, and images are created and generated using Canva and Gemini AI", foreground='gray',background='#F2E1C9', font=("Arial", 8))
Footer.place(relx=0.5, rely=1.0, anchor="s", y=-7)

# Call display_home() to show the Home screen by default when the app starts
display_home()

ads()

# Run the main loop
dash_board.mainloop()
