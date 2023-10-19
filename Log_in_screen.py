import customtkinter as ctk
from PIL import Image, ImageTk

#set background
ctk.set_appearance_mode("light")

# Create the application window
root = ctk.CTk()
root.title("Display")
root.geometry("600x600")
root.state("normal")

def login():
    print("Log in successfully")

def rememberUser():
    print("Remembered in the system")

def faceID_Login():
    print("Using FaceID")

#create big frame
frame = ctk.CTkFrame(master=root)
frame.pack(pady=100, padx=10, expand=True)

#create name of page
label = ctk.CTkLabel(master=frame, text="Log in", font=("Arial", 24), text_color="#117ACA")
label.pack(pady=12, padx=10)

#create username box
entry1 = ctk.CTkEntry(master=frame, placeholder_text="Enter your User ID")
entry1.pack(pady=12, padx=10)
#create password box
entry2 = ctk.CTkEntry(master=frame, placeholder_text="Enter your Password", show="*")
entry2.pack(pady=12, padx=10)

#create remember me checkbox
checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me", command=rememberUser)
checkbox.pack(pady=12, padx=10)

#create use token checkbox
button = ctk.CTkCheckBox(master=frame, text="Face ID", command=faceID_Login)
button.pack(pady=12, padx=80)

#create log in button
button1 = ctk.CTkButton(master=frame, text="Log On", command=login)
button1.pack(pady=30, padx=10)

#Run the application
root.mainloop()






