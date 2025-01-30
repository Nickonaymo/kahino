from tkinter import *
from tkinter import PhotoImage

import customtkinter
import customtkinter as ctk
from customtkinter import CTk, CTkFrame, CTkComboBox, CTkButton
from PIL import Image


customtkinter.set_appearance_mode("light")

# Landing Page/Main Window
landingPage = CTk()
landingPage.geometry("1366x768")
landingPage.title("Luxury Salon Booking/Appointment System")
landingPage.configure(fg_color="#E6E6FA")

# Ensure the file path is correct
icon_file = "windowIcon .png"
try:
    windowIcon = PhotoImage(file=icon_file)
    landingPage.iconphoto(True, windowIcon)
except Exception as e:
    print(f"Error loading icon: {e}")

#================================================================================================
# Main Frame
mainFrame= CTkFrame(master=landingPage, fg_color="white", width=1300, height=650)
mainFrame.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

salonLogo = customtkinter.CTkImage(light_image=Image.open('salonLogo.png'), size=(300,100))
salonLabel = customtkinter.CTkLabel(master=mainFrame, text="", image=salonLogo)
salonLabel.place(x=0,y=8)

# Combo Boxes (Options)
about = ctk.CTkComboBox(master=mainFrame, values=["About", "Owner", "Salon"], font=("Arial", 14))
about.configure(fg_color="white", button_color="gray", state="readonly")
about.place(x=350, y=45)

overview = CTkComboBox(master=mainFrame, values=["Salon OverView", "Pricing","Salon"], font=("Arial", 14) )
overview.configure(fg_color="white", button_color="gray", state="readonly")
overview.place(x=500, y=45)

service = CTkComboBox(master=mainFrame, values=["Service Details", "Owner","Salon"], fg_color="white", font=("Arial", 14) )
service.configure(fg_color="white", button_color="gray", state="readonly")
service.place(x=650, y=45)

appointment = CTkComboBox(master=mainFrame, values=["Appointment", "Owner","Salon"], fg_color="white", font=("Arial", 14) )
appointment.configure(fg_color="white", button_color="gray", state="readonly")
appointment.place(x=800, y=45)

aboutSalon = CTkButton(master=mainFrame,text="Contact",text_color="black", fg_color="white", font=("Arial", 14) )
aboutSalon.place(x=950, y=45)

#================================================================================================
# Options Frame
optionsFrame= CTkFrame(master=mainFrame, fg_color="white", width=1300, height=600)
optionsFrame.place(x=0, y=100)

# Add image file
ads = PhotoImage(file="ads.png")

# Create Canvas
canvas = Canvas(optionsFrame, width=1300, height=600)
canvas.pack(fill="both", expand=True)

# Display image
canvas.create_image(0, 0, image=ads, anchor="nw")


landingPage.mainloop()

