from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import Tk, Label
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

# Function to clear the scrollable frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_frame(frame):
    # Hide all other frames
    for f in [scrollable_frame_home, scrollable_frame_pizza, scrollable_frame_burger,
              scrollable_frame_fries, scrollable_frame_drinks]:
        f.place_forget()
    # Show the selected frame
    frame.place(x=180, y=120)

# Scrollable Frames
scrollable_frame_home = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_pizza = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_burger = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_fries = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_drinks = customtkinter.CTkScrollableFrame(dash_board, width=600, height=380)
scrollable_frame_home.place(x=180, y=120)

# Function to create a button with an image and text for two columns in a scrollable frame
def home_button(parent, image_path, button_text, row, column):
    try:
        icon_photo = PhotoImage(file=image_path)
        icon_photo_resized = icon_photo.subsample(3, 3)
        button = Button(
            parent,
            text=button_text,
            fg='gray',
            font=('Arial', 8),
            image=icon_photo_resized,
            compound='top',
            bg=dash_board.cget('bg'),
            activebackground=dash_board.cget('bg'),
            relief="flat"
        )
        button.image = icon_photo_resized
        button.grid(row=row, column=column, padx=10, pady=10)
    except Exception as e:
        print(f"Error creating button {button_text}: {e}")

# Function to display the home buttons in two columns (now with row/column logic)
def display_home():
    clear_frame(scrollable_frame_home)

    # Button placement logic: Column 0 and 1, after every 2 buttons move to next row.
    buttons = [
        ('classic.png', '₱85: Classic Burger'),
        ('medium.png', '₱65: Medium Fries'),
        ('_Ham and Cheese.png', '₱120: Ham and Cheese Pizza'),
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
        ('classic.png', 'Classic Burger'),
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
        icon_photo_resized = icon_photo.subsample(10, 10)
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
create_button('home.png', 'Home', 100, 120, command=display_home)
create_button('pizza.png', 'Pizza', 100, 200, command=display_pizzas)
create_button('burger.png', 'Burger', 100, 280, command=display_burgers)
create_button('fries.png', 'Fries', 100, 360, command=display_fries)
create_button('drinks.png', 'Drinks', 100, 440, command=display_drinks)

# Payment Frame
payment_frame = Frame(dash_board, width=250, height=450, bg='light gray', bd=5)
payment_frame.place(x=840, y=0)

# Divider
divider = Frame(dash_board, bg="dark gray", height=2, width=210)
divider.place(x=860, y=400)  # Use place() to position the divider

# Total Frame
total_frame = Frame(dash_board, bg="white")
total_frame.place(x=860, y=420)

# Label to show the total amount
total_label = Label(total_frame, text="Total: ₱0.00", fg="black", font=("Arial", 12), bg="white")
total_label.place(x=900, y=420)

# Place Order frame
Button(dash_board, width=20, height=2, text='Check out', bg='#DB7921', fg='white', font=('Arial', 15, 'bold'), border=0).place(x=840, y=460)

# Footer section (text or images)
footer_frame = Frame(dash_board, bg='#F2E1C9', height=10)
footer_frame.place(relx=0, rely=1, relwidth=1, anchor="sw")

# Footer text
footer_text = Label(footer_frame, text="© 2024 | Icons, backgrounds, and images are created and generated using Canva and Gemini AI", bg='#F2E1C9', fg="gray", font=("Arial", 8))
footer_text.pack(pady=5)

# Call display_home() to show the Home screen by default when the app starts
display_home()

# Run the main loop
dash_board.mainloop()