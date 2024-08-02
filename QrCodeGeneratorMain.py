from tkinter import *
import qrcode
from PIL import Image, ImageTk  # Import PIL modules for image handling

# Initialize the main window
root = Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False, False)

# Set the window icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

def generate():
    name = title.get()
    text = entry.get()
    
    if name and text:  # Ensure both name and text fields are not empty
        # Generate QR code
        qr = qrcode.make(text)
        qr_path = f"Qrcode/{name}.png"
        qr.save(qr_path)
        
        # Open and display the QR code image
        qr_image = Image.open(qr_path)
        qr_image = qr_image.resize((200, 200))  # Resize for better display
        qr_image = ImageTk.PhotoImage(qr_image)
        
        Image_view.config(image=qr_image)
        Image_view.image = qr_image  # Keep a reference to avoid garbage collection
    else:
        # Handle the case where name or text is empty
        print("Please enter both title and text.")

# Create a label for displaying the QR code
Image_view = Label(root, bg="#AE2321")
Image_view.pack(padx=50, pady=10, side=RIGHT)

# Label and Entry for the QR code title
Label(root, text="Title", fg="white", bg="#AE2321", font=("Arial", 15)).place(x=50, y=170)
title = Entry(root, width=13, font="Arial 15")
title.place(x=50, y=200)

# Entry for the text to be encoded in the QR code
entry = Entry(root, width=28, font="Arial 15")
entry.place(x=50, y=250)

# Button to trigger the QR code generation
Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=300)

root.mainloop()
