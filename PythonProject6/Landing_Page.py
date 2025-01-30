import customtkinter
from customtkinter import CTk, CTkFrame, CTkComboBox, CTkButton, CTkImage, CTkLabel
from PIL import Image
import os


class LandingPage(CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("light")

        # Landing Page/Main Window
        self.geometry("1366x768")
        self.title("Luxury Salon Booking/Appointment System")
        self.configure(fg_color="#E6E6FA")

        # Configure grid to make the background and landingFrame properly responsive
        self.grid_rowconfigure(0, weight=0)

        # Landing Frame
        landing_frame = CTkFrame(master=self, fg_color="red", width=1300, height=650)
        landing_frame.grid(padx=15, pady=15)

        # Salon Logo
        logo_path = 'salonLogo.png'
        if os.path.exists(logo_path):
            salon_logo = CTkImage(light_image=Image.open(logo_path), size=(300, 100))
            CTkLabel(landing_frame, text="", image=salon_logo).place(x=0, y=8)
        else:
            print(f"Error: {logo_path} not found!")

        # ComboBox Options
        combo_options = [
            ("About", 350),
            ("Salon Overview", 500),
            ("Service Details", 650),
            ("Appointment", 800),
        ]

        for text, x_position in combo_options:
            combo_box = CTkComboBox(
                master=landing_frame,
                values=[text, "Owner", "Salon"],
                font=("Arial", 14),
                fg_color="white",
                button_color="gray",
                state="readonly",
            )
            combo_box.place(x=x_position, y=45)

        # Contact Button
        contact_button = CTkButton(
            master=landing_frame,
            text="Contact",
            text_color="black",
            fg_color="white",
            font=("Arial", 14),
        )
        contact_button.place(x=950, y=45)

        # Options Frame
        options_frame = CTkFrame(master=landing_frame, fg_color="white", width=1300, height=600)
        options_frame.place(x=0, y=100)

        # Background Image in Options Frame
        ads_path = "ads.png"
        if os.path.exists(ads_path):
            ads_image = CTkImage(light_image=Image.open(ads_path), size=(1300, 600))
            CTkLabel(options_frame, text="", image=ads_image).pack(fill="both", expand=True)
        else:
            print(f"Error: {ads_path} not found!")


# Run the Application
if __name__ == "__main__":
    app = LandingPage()
    app.mainloop()
