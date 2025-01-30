# Importing Libraries Needed
import tkinter
from tkinter import Checkbutton, Button
import customtkinter
from PIL import Image
from PyQt6.QtGui import QCursor

# Configure customtkinter appearance
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

# Create the main window
loginPage = customtkinter.CTk()
loginPage.geometry("1366x768")
loginPage.title("Login Page")

# Open and load the image using Pillow
backgroundImg = Image.open("bg.png")
backgroundImg_resized = backgroundImg.resize((1366, 768), Image.Resampling.LANCZOS)  # High-quality resizing

# Convert the image for use in customtkinter
img1_ctk = customtkinter.CTkImage(light_image=backgroundImg_resized, size=(1366, 768))

# Create a background label with the image
background = customtkinter.CTkLabel(master=loginPage, image=img1_ctk, text="")
background.grid(row=0, column=0, sticky="nsew")  # Make the image cover the entire window

# Configure grid to make the background and loginFrame properly responsive
loginPage.grid_rowconfigure(0, weight=1)
loginPage.grid_columnconfigure(0, weight=1)
background.grid_rowconfigure(0, weight=1)
background.grid_columnconfigure(0, weight=1)

# Logo Frame
logoFrame = customtkinter.CTkFrame(master=background, width=500, height=500, corner_radius=20, fg_color="#F5F5DC", bg_color="#fff7ad")
logoFrame.grid(row=0, column=0, pady=100, padx=200, sticky="news")

# Logo Image
logoImg = Image.open("Logo.png")
logoImg_resize = logoImg.resize((450, 450), Image.Resampling.LANCZOS)

img2_ctk = customtkinter.CTkImage(light_image=logoImg_resize, size=(450, 450))

# Create a background label with the image
logo = customtkinter.CTkLabel(master=logoFrame, image=img2_ctk, text="")
logo.grid(row=0, column=0, pady=40, padx=20, sticky="ns")

# Login Frame
loginFrame = customtkinter.CTkFrame(master=logoFrame, corner_radius=20, bg_color="#F5F5DC", fg_color="#E6E6FA")
loginFrame.grid(row=0, column=35, pady=40,padx=20, sticky="news")

# Configure rows in loginFrame to adjust spacing
loginFrame.grid_rowconfigure(0, weight=1)  # Space above the content
loginFrame.grid_rowconfigure(1, weight=0)  # Greetings
loginFrame.grid_rowconfigure(2, weight=0)  # Username
loginFrame.grid_rowconfigure(3, weight=0)  # Password
loginFrame.grid_rowconfigure(4, weight=0)  # Checkbox and forgot password
loginFrame.grid_rowconfigure(5, weight=0)  # Login button
loginFrame.grid_rowconfigure(6, weight=0)  # Signup prompt
loginFrame.grid_rowconfigure(7, weight=1)  # Space between content and footer

# Add a title label to the login frame
greetings = customtkinter.CTkLabel(master=loginFrame, text="\n       Welcome To Luxury Salon!       ", font=("Montserrat", 24, "bold"), text_color="black")
greetings.grid()

username_entry = customtkinter.CTkEntry(master=loginFrame, width=300, height=40, corner_radius=10, placeholder_text="Username")
username_entry.grid(pady=20)

password_entry = customtkinter.CTkEntry(master=loginFrame, width=300, height=40, corner_radius=10, placeholder_text="Password", show="*")
password_entry.grid()

# Checkbox for Show/Hide Password
show_password_checkbox = Checkbutton(master=loginFrame, text="Show Password", fg="#57a1f8", bg="#E6E6FA", font=("Arial", 8))
show_password_checkbox.grid(padx=60, sticky="w")

# Forgot Password Button
forgot_password = Button(master=loginFrame, width=13, text="Forgot Password?", border=0, bg='#E6E6FA', fg='#57a1f8')
forgot_password.grid(row=3, padx=60, sticky="e")

# Add login button
login_button = customtkinter.CTkButton(master=loginFrame, text="Login", width=200, height=40, corner_radius=10, fg_color="green")
login_button.grid(pady=10, padx=52, sticky="we")

# Sign up prompt
signupPrompt = customtkinter.CTkLabel(master=loginFrame, text="Don't have an account?", font=('Arial', 12))
signupPrompt.grid(row=5, padx=105 ,sticky="w")

# Sign up Button
sign_up = Button(master=loginFrame, width=6, text='Sign up', border=0, bg='#E6E6FA', cursor='hand2', fg='#57a1f8')
sign_up.grid(row=5, padx=120, sticky="e")

# Footer
footer = customtkinter.CTkLabel(master=loginFrame, text="© 2024 | Icons, backgrounds, and images are created using Canva.", font=('Arial', 10))
footer.grid(column=0, row=7, sticky="s")

# Run the app
loginPage.mainloop()
