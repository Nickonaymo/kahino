import tkinter
from tkinter import Checkbutton, Button
import customtkinter
from customtkinter import CTk, CTkFrame, CTkComboBox, CTkButton, CTkImage, CTkLabel

from PIL import Image
import os

class LandingPage:
    def __init__(self, root):
        # Configure customtkinter appearance
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        self.landingPage = root
        self.landingPage.geometry("1366x768")
        self.landingPage.title("Beauty Salon System")

        self.landing_frame()

    def landing_frame(self):
        # Configure the root grid to center the frame
        self.landingPage.grid_rowconfigure(0, weight=1)  # Add weight to top row
        self.landingPage.grid_rowconfigure(1, weight=0)  # Add weight to bottom row
        self.landingPage.grid_columnconfigure(0, weight=1)  # Add weight to left column
        self.landingPage.grid_columnconfigure(1, weight=0)  # Add weight to right column

        # Landing Frame
        landing_frame = CTkFrame(master=self.landingPage, fg_color="white", width=1300, height=650, corner_radius=20)
        landing_frame.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        # Salon Logo
        logo_path = 'salonLogo.png'
        if os.path.exists(logo_path):
            salon_logo = customtkinter.CTkImage(light_image=Image.open(logo_path), size=(300, 100))
            logo_label = customtkinter.CTkLabel(landing_frame, text="", image=salon_logo)
            logo_label.grid(pady=10,padx=20, sticky="nw")  # Add some space above and below
        else:
            # Display a placeholder text if the logo is missing
            placeholder_logo = customtkinter.CTkLabel(landing_frame, text="Luxury Salon Logo", font=("Arial", 24, "bold"), corner_radius=20)
            placeholder_logo.grid(row=0, column=0, sticky="nw")

        # Options Frame
        options_frame = CTkFrame(master=landing_frame, fg_color="#f0f0f0", width=1300, height=600, corner_radius=20)
        options_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))

        # Configure grid within landing_frame for proportional spacing
        landing_frame.grid_rowconfigure(0, weight=0)  # Logo row
        landing_frame.grid_rowconfigure(1, weight=1)  # Options frame row
        landing_frame.grid_columnconfigure(0, weight=1)  # Center column

        # Background Image in Options Frame
        ads_path = "ads.png"
        if os.path.exists(ads_path):
            ads_image = customtkinter.CTkImage(light_image=Image.open(ads_path), size=(1300, 600))
            customtkinter.CTkLabel(options_frame, text="", image=ads_image).grid(sticky="nsew")
        else:
            print(f"Error: {ads_path} not found!")

class SignUp:
    def __init__(self, root):

        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        self.signupPage = root
        self.signupPage.geometry("1366x768")

class LoginPage(CTk):
    def __init__(self, root):

        # Configure customtkinter appearance
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("blue")

        self.loginPage = root
        self.loginPage.geometry("1366x768")
        self.loginPage.title("Beauty Salon Login System")

        # Open and load the background image using Pillow
        self.backgroundImg = Image.open("bg.png")
        self.backgroundImg_resized = self.backgroundImg.resize((1366, 768), Image.Resampling.LANCZOS)

        # Convert the image for use in customtkinter
        self.img1_ctk = customtkinter.CTkImage(light_image=self.backgroundImg_resized, size=(1366, 768))

        # Create a background label with the image
        self.background = customtkinter.CTkLabel(master=self.loginPage, image=self.img1_ctk, text="")
        self.background.grid(row=0, column=0, sticky="nsew")

        # Configure grid to make the background and loginFrame properly responsive
        self.loginPage.grid_rowconfigure(0, weight=1)
        self.loginPage.grid_columnconfigure(0, weight=1)
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(0, weight=1)

        self.create_logo_frame()
        self.create_login_frame()

    def create_logo_frame(self):
        # Logo Frame
        self.logoFrame = customtkinter.CTkFrame(master=self.background, width=500, height=500, corner_radius=20, fg_color="#F5F5DC", bg_color="#fff7ad")
        self.logoFrame.grid(row=0, column=0, pady=100, padx=200, sticky="news")

        # Logo Image
        self.logoImg = Image.open("Logo.png")
        self.logoImg_resize = self.logoImg.resize((450, 450), Image.Resampling.LANCZOS)

        self.img2_ctk = customtkinter.CTkImage(light_image=self.logoImg_resize, size=(450, 450))

        # Create a background label with the image
        self.logo = customtkinter.CTkLabel(master=self.logoFrame, image=self.img2_ctk, text="")
        self.logo.grid(row=0, column=0, pady=40, padx=20, sticky="ns")

    def create_login_frame(self):
        # Login Frame
        self.loginFrame = customtkinter.CTkFrame(master=self.logoFrame, corner_radius=20, bg_color="#F5F5DC", fg_color="#E6E6FA")
        self.loginFrame.grid(row=0, column=35, pady=40, padx=20, sticky="news")

        # Configure rows in loginFrame to adjust spacing
        self.loginFrame.grid_rowconfigure(0, weight=1)  # Space above the content
        self.loginFrame.grid_rowconfigure(1, weight=0)  # Greetings
        self.loginFrame.grid_rowconfigure(2, weight=0)  # Username
        self.loginFrame.grid_rowconfigure(3, weight=0)  # Password
        self.loginFrame.grid_rowconfigure(4, weight=0)  # Checkbox and forgot password
        self.loginFrame.grid_rowconfigure(5, weight=0)  # Login button
        self.loginFrame.grid_rowconfigure(6, weight=0)  # Signup prompt
        self.loginFrame.grid_rowconfigure(7, weight=1)  # Space between content and footer
        self.add_login_widgets()

    def add_login_widgets(self):
        # Add a title label to the login frame
        self.greetings = customtkinter.CTkLabel(master=self.loginFrame, text="\n       Welcome To Luxury Salon!       ", font=("Montserrat", 24, "bold"), text_color="black")
        self.greetings.grid()

        # Username and Password Entries
        self.username_entry = customtkinter.CTkEntry(master=self.loginFrame, width=300, height=40, corner_radius=10, placeholder_text="Username")
        self.username_entry.grid(pady=20)

        self.password_entry = customtkinter.CTkEntry(master=self.loginFrame, width=300, height=40, corner_radius=10, placeholder_text="Password", show="*")
        self.password_entry.grid()

        # Checkbox for Show/Hide Password
        self.show_password_checkbox = Checkbutton(master=self.loginFrame, text="Show Password", fg="#57a1f8", bg="#E6E6FA", font=("Arial", 8))
        self.show_password_checkbox.grid(padx=60, sticky="w")

        # Forgot Password Button
        self.forgot_password = Button(master=self.loginFrame, width=13, text="Forgot Password?", border=0, bg='#E6E6FA', fg='#57a1f8')
        self.forgot_password.grid(row=3, padx=60, sticky="e")

        # Add login button
        self.login_button = customtkinter.CTkButton(master=self.loginFrame, text="Login", width=200, height=40, corner_radius=10, fg_color="green")
        self.login_button.grid(pady=10, padx=52, sticky="we")

        # Sign up prompt
        self.signupPrompt = customtkinter.CTkLabel(master=self.loginFrame, text="Don't have an account?", font=('Arial', 12))
        self.signupPrompt.grid(row=5, padx=105, sticky="w")

        # Sign up Button
        self.sign_up = Button(master=self.loginFrame, width=6, text='Sign up', border=0, bg='#E6E6FA', cursor='hand2', fg='#57a1f8')
        self.sign_up.grid(row=5, padx=120, sticky="e")

        # Footer
        self.footer = customtkinter.CTkLabel(master=self.loginFrame, text="© 2024 | Icons, backgrounds, and images are created using Canva.", font=('Arial', 10))
        self.footer.grid(column=0, row=7, sticky="s")

class BeautySalonSystem(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1366x768")
        self.title("Beauty Salon Management System")
        self.frames = {}

        # Initialize frames
        for F in (LoginPage, LandingPage):
            frame = F(self)
            self.frames[F] = frame

        # Show the initial frame (LoginPage)
        self.show_frame(LoginPage)

    def show_frame(self, frame_class):
        """Bring the specified frame to the front."""
        frame = self.frames[frame_class]
        # Access the underlying tkinter Frame to use tkraise()
        frame.tkraise()

if __name__ == "__main__":
    app = BeautySalonSystem()
    app.mainloop()