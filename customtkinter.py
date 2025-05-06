import customtkinter as ctk

# Create the main window
ctk.set_appearance_mode("dark")  # Themes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

app = ctk.CTk()  # Create window
app.title("CustomTkinter in VS Code")
app.geometry("400x300")

# Create a label
label = ctk.CTkLabel(app, text="Hello, CustomTkinter!", font=("Arial", 18))
label.pack(pady=20)

# Create a button
def button_click():
    label.configure(text="Button Clicked!")

button = ctk.CTkButton(app, text="Click Me", command=button_click)
button.pack(pady=10)

# Run the app
app.mainloop()
