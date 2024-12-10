from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter

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

def signin_display():
    frame = Frame(dash_board, width=270, height=410, bg='light gray', bd=5, )
    frame.place(x=820, y=120)

    heading = Label(frame, text='Log In', fg='white', bg='#DB7921', font=('Arial', 24, 'bold'))
    heading.place(x=100, y=10)

    # Username Textbox
    user = Entry(frame, width=35, font=('Arial', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')

    # Line under username
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # Password Textbox
    password = Entry(frame, width=35, bg='white', font=('Arial', 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')

    # Line under password
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

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

def show_frame(frame):
    # Hide all other frames
    for f in [scrollable_frame_home, scrollable_frame_pizza, scrollable_frame_burger,
              scrollable_frame_fries, scrollable_frame_drinks]:
        f.place_forget()
    # Show the selected frame
    frame.place(x=180, y=120)

# Scrollable Frames for items
scrollable_frame_home = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_pizza = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_burger = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_fries = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_drinks = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_home.place(x=180, y=120)

# Dictionary to track selected items and their quantities
selected_items = {}

def refresh_selected_items():
    # Clear the current display
    for widget in selected_items_panel.winfo_children():
        widget.destroy()

    # Add all selected items to the display
    for idx, (item_name, item_data) in enumerate(selected_items.items()):
        item_frame = Frame(selected_items_panel, bg='white', bd=2, relief="groove")
        item_frame.grid(row=idx, column=0, sticky="ew", padx=5, pady=5)

        # Create a label showing the item name, quantity, and total price
        item_label = Label(
            item_frame,
            text=f"{item_name} x{item_data['quantity']} - ₱{item_data['quantity'] * item_data['price']:.2f}",
            font=("Arial", 8),
            bg="white",
        )
        item_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Create a remove button to remove the item from selected items
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

    # Update subtotal and total
    update_totals()

# Function to remove one instance of an item from selected items
def remove_from_selected_items(item_name):
    """
    Removes one instance of an item from the selected_items dictionary.
    If the quantity becomes 0, the item is completely removed.
    """
    if item_name in selected_items:
        # Decrease quantity by 1
        selected_items[item_name]['quantity'] -= 1
        # If quantity is 0 or less, remove the item
        if selected_items[item_name]['quantity'] <= 0:
            del selected_items[item_name]
        refresh_selected_items()  # Refresh the display after the update
    else:
        print(f"Item '{item_name}' not found in selected items.")  # Debug message or handle appropriately

# Function to add items to the selected items
def add_to_selected_items(item_name, item_price):
    if item_name in selected_items:
        # Increase quantity by 1
        selected_items[item_name]['quantity'] += 1
    else:
        # Add new item with price and quantity 1
        selected_items[item_name] = {'price': item_price, 'quantity': 1}

    # Refresh the selected items display
    refresh_selected_items()

# Function to calculate and update totals
def update_totals():
    subtotal = sum(data['price'] * data['quantity'] for data in selected_items.values())
    delivery_fee = 50 if subtotal > 0 else 0  # Example delivery charge logic
    total_amount = subtotal + delivery_fee

    # Update labels
    sub_total.config(text=f"Sub Total: ₱{subtotal:.2f}")
    delivery_charge.config(text=f"Delivery Charges: ₱{delivery_fee:.2f}")
    total.config(text=f"Total: ₱{total_amount:.2f}")

# Function to clear the scrollable frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

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
            command=lambda: add_to_selected_items(item_name, item_price),
        )
        button.image = icon_photo_resized
        button.grid(row=row, column=column, padx=10, pady=10)
    except Exception as e:
        print(f"Error creating button {button_text}: {e}")


# Scrollable Frames for items
scrollable_frame_home = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_home.place(x=180, y=120)

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

# Create the buttons using the function
create_button('Login.png', 'Login', 100, 120, command =signin_display)
create_button('home.png', 'Home', 100, 180, command=display_home)
create_button('pizza.png', 'Pizza', 100, 240, command=display_pizzas)
create_button('burger.png', 'Burger', 100, 300, command=display_burgers)
create_button('fries.png', 'Fries', 100, 360, command=display_fries)
create_button('drinks.png', 'Drinks', 100, 420, command=display_drinks)

# Scrollable Frames for chosen items
selected_items_panel = customtkinter.CTkScrollableFrame(dash_board, width=250, height=1)
selected_items_panel.place(x=820, y=120)

Orders = ttk.Label(dash_board, text="Orders:", foreground='white', background='#DB7921', font=("Helvetica", 18, 'bold'))
Orders.place(x=850, y=80)

# Divider
divider = tk.Canvas(dash_board, background="light gray", height=1, width=220)
divider.place(x=850, y=400)

# Label to show the sub-total amount
sub_total = ttk.Label(dash_board, text="Sub Total:                      ₱0.00", foreground="gray", font=("Arial", 12))
sub_total.place(x=860, y=340)

# Label to show the sub-total amount
delivery_charge = ttk.Label(dash_board, text="Delivery Charges:         ₱0.00", foreground="gray",font=("Arial", 12))
delivery_charge.place(x=860, y=370)

# Label to show the total amount
total = ttk.Label(dash_board, text="Total:                              ₱0.00", foreground="gray", font=("Arial", 12))
total.place(x=860, y=420)

# Place Order frame
Button(dash_board, width=20, height=2, text='Place Order', bg='#DB7921', foreground='white',font=('Arial', 15, 'bold'), border=0).place(x=840, y=460)

# Footer
Footer = ttk.Label(dash_board, text="© 2024 | Icons, backgrounds, and images are created and generated using Canva and Gemini AI", foreground='gray',background='#F2E1C9', font=("Arial", 8))
Footer.place(relx=0.5, rely=1.0, anchor="s", y=-7)

# Call display_home() to show the Home screen by default when the app starts
display_home()

# Run the main loop
dash_board.mainloop()
