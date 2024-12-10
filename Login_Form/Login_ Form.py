import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import re
from PIL import ImageTk, Image
from PIL import ImageTk, ImageTk
from tkinter import Tk, Label

BG_COLOR = 'lightblue'
FRAME_BG = 'white'
HEADING_COLOR = '#57a1f8'
TEXT_COLOR = 'black'
HEADING_FONT = ('Microsoft YaHei UI Light', 30, 'bold')
LABEL_FONT = ('Microsoft YaHei UI Light', 12)
BUTTON_FONT = ('Microsoft YaHei UI Light', 13, 'bold')
ENTRY_WIDTH = 30
BUTTON_WIDTH = 15

# File paths
requests_file = "requests.json"
users_file = "users.json"

try:
    with open(users_file, "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

# Email validation function using regex
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Function to handle sign-up
def sign_up(username_entry, password_entry, confirm_password_entry, email_entry):
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    email = email_entry.get()

    # Check if all fields are filled
    if not username or not password or not confirm_password or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Validate email format using regex
    if not is_valid_email(email):
        messagebox.showerror("Error", "Please enter a valid email address!")
        return

    # Check if the username or email already exists
    if any(user["username"] == username or user["email"] == email for user in users):
        messagebox.showerror("Error", "Username or Email already exists!")
        return

    # Add user to the list of users
    users.append({"username": username, "password": password, "email": email})

    # Save users to the file
    with open(users_file, "w") as file:
        json.dump(users, file)

    # Show success message and clear the form
    messagebox.showinfo("Success", "Please wait for Admin approval")
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    confirm_password_entry.delete(0, 'end')
    email_entry.delete(0, 'end')

# Function to toggle password visibility
def toggle_password_visibility(password_entry, confirm_password_entry, var):
    if var.get():
        password_entry.config(show="")  # Show password
        confirm_password_entry.config(show="")  # Show confirm password
    else:
        password_entry.config(show="*")  # Hide password
        confirm_password_entry.config(show="*")  # Hide confirm password

# Function to open the sign-up window
def register():
    # Create a new Toplevel window
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up Form")
    signup_window.geometry("925x500+300+200")
    signup_window.configure(bg=BG_COLOR)
    signup_window.resizable(False, False)

    # Frame for Form
    frame = tk.Frame(signup_window, bg=FRAME_BG, padx=20, pady=20, relief='raised', bd=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Heading
    heading = tk.Label(frame, text="Create an Account", fg=HEADING_COLOR, bg=FRAME_BG, font=HEADING_FONT)
    heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Username
    tk.Label(frame, text="Username:", font=LABEL_FONT, fg=TEXT_COLOR, bg=FRAME_BG).grid(row=1, column=0, sticky="w", padx=10, pady=10)
    username_entry = tk.Entry(frame, width=ENTRY_WIDTH)
    username_entry.grid(row=1, column=1, padx=10, pady=10)

    # Password
    tk.Label(frame, text="Password:", font=LABEL_FONT, fg=TEXT_COLOR, bg=FRAME_BG).grid(row=2, column=0, sticky="w", padx=10, pady=10)
    password_entry = tk.Entry(frame, width=ENTRY_WIDTH, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    # Confirm Password
    tk.Label(frame, text="Confirm Password:", font=LABEL_FONT, fg=TEXT_COLOR, bg=FRAME_BG).grid(row=3, column=0, sticky="w", padx=10, pady=10)
    confirm_password_entry = tk.Entry(frame, width=ENTRY_WIDTH, show="*")
    confirm_password_entry.grid(row=3, column=1, padx=10, pady=10)

    # Email
    tk.Label(frame, text="Email:", font=LABEL_FONT, fg=TEXT_COLOR, bg=FRAME_BG).grid(row=4, column=0, sticky="w", padx=10, pady=10)
    email_entry = tk.Entry(frame, width=ENTRY_WIDTH)
    email_entry.grid(row=4, column=1, padx=10, pady=10)

    # Show Password Checkbox
    show_password_var = tk.BooleanVar()
    show_password_checkbox = tk.Checkbutton(frame, text="Show Password", variable=show_password_var, bg=FRAME_BG, fg=HEADING_COLOR,command=lambda: toggle_password_visibility(password_entry, confirm_password_entry, show_password_var))
    show_password_checkbox.grid(row=5, column=0, columnspan=2, pady=10)

    # Function to handle sign-up
    def sign_up():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        email = email_entry.get()

        # Check if all fields are filled
        if not username or not password or not confirm_password or not email:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Validate email format using regex
        if not is_valid_email(email):
            messagebox.showerror("Error", "Please enter a valid email address!")
            return

        # Check if the username or email already exists
        if any(user["username"] == username or user["email"] == email for user in users):
            messagebox.showerror("Error", "Username or Email already exists!")
            return

        # Add user to the list of users
        users.append({"username": username, "password": password, "email": email})

        # Save users to the file
        with open(users_file, "w") as file:
            json.dump(users, file)

        # Show success message and clear the form
        messagebox.showinfo("Success", "Please wait for Admin approval")
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        confirm_password_entry.delete(0, 'end')
        email_entry.delete(0, 'end')

    # Submit Button
    button_submit = tk.Button(frame, text="Sign Up", width=BUTTON_WIDTH, command=sign_up, bg=HEADING_COLOR, fg="white",border=0, font=BUTTON_FONT)
    button_submit.grid(row=6, column=0, columnspan=2, pady=20)
    # Footer
    footer = tk.Label(signup_window, text="© 2024 Advance Programming. All Rights Reserved.", bg=BG_COLOR, fg="gray", font=('Arial', 10))
    footer.pack(side="bottom", pady=10)

def retrieve_password():
    # Password Recovery Form
    password_recovery_window = Tk()
    password_recovery_window.title('Password Retrieval')
    password_recovery_window.geometry("925x500+300+200")
    password_recovery_window.configure(bg='lightblue')
    password_recovery_window.resizable(False, False)

    frame = Frame(password_recovery_window, width=350, height=350, bg='white', relief=RAISED, bd=5)
    frame.place(x=280, y=70)

    heading = Label(frame, text='Password Recovery', fg='#57a1f8', bg='white', font=('Arial', 20, 'bold'))
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
    Button(frame, width=39, pady=10, text='Submit', bg='#57a1f8', fg='white', command=submit, border=0).place(x=35, y=210)

#================================================================================================================================================
# Main Display
root = Tk()
root.title('Advance Programming')
root.geometry("925x500+300+200")
root.configure(bg='lightblue')  # Lighter background color for a more modern look
root.resizable(False, False)

frame = Frame(root, width=350, height=350, bg='white', relief=RAISED, bd=5)
frame.place(x=280, y=70)

heading = Label(frame, text='Log In', fg='#57a1f8', bg='white', font=('Arial', 24, 'bold'))
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
#================================================================================================================================================

# Function for focus in and out (Textbox behavior)
def on_enter_user(e):
    user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Username')

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

max_attempt = 3
incorrect_attempts = 0

# Function to Disable Login Form
def disable_form():
    user.config(state=DISABLED)
    password.config(state=DISABLED)
    sign_up.config(state=DISABLED)

    messagebox.showerror("Too Many Attempts", "You have reached the maximum number of login attempts. Please try again later.")

# Sign in Button Command
def signin():
    global incorrect_attempts

    if incorrect_attempts >= max_attempt:
        disable_form()
        return

    username = user.get()
    password1 = password.get()

    if username == 'admin' and password1 == '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen, text='Hello! Welcome to Python Programming', bg='#fff', font=('Arial', 35, 'bold')).pack(expand=True)


        root.withdraw()
        screen.mainloop()

    elif username != 'admin' and password1 == '1234':
        messagebox.showerror('Invalid', "Incorrect username")
        incorrect_attempts += 1

    elif username == 'admin' and password1 != '1234':
        messagebox.showerror('Invalid', "Incorrect password")
        incorrect_attempts += 1

    elif username == '':
        messagebox.showerror('Invalid', "Username is empty")
        incorrect_attempts += 1

    else:
        messagebox.showerror('Invalid', "Invalid username and password")
        incorrect_attempts += 1

    if incorrect_attempts == max_attempt:
        disable_form()

# Boolean variable to store the checkbox state
show_password_var = BooleanVar()

# Function to update password visibility based on checkbox
def toggle_password_visibility2():
    if show_password_var.get():
        password.config(show='')  # Show password (text input)
    else:
        password.config(show='*')  # Hide password (show '*' characters)

# Forgot Password Button
forgot_password = Button(frame, width=20, text='Forgot Password?', border=0, bg='white', command=retrieve_password, cursor='hand2', fg='#57a1f8')
forgot_password.place(x=195, y=181)

# Checkbox for Show/Hide Password
show_password_checkbox = Checkbutton(frame, text="Show Password", variable=show_password_var, bg='white', fg='#57a1f8', command=toggle_password_visibility2)
show_password_checkbox.place(x=30, y=180)

# Sign in Button
Button(frame, width=39, pady=10, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=210)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Arial', 9))
label.place(x=75, y=270)

# Sign up Button
sign_up = Button(frame, width=6, text='Sign up', border=0, command=register, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

# Footer
footer = tk.Label(root, text="© 2024 Advance Programming. All Rights Reserved.", bg=BG_COLOR, fg="gray", font=('Arial', 10))
footer.pack(side="bottom", pady=10)

root.mainloop()