import customtkinter as ctk
from ui_elements import UIElements
from qr_generator import QRGenerator
from qr_scanner import QRScanner

class QRCodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # App-Settings
        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()
        app_width = int(SCREEN_WIDTH * 0.75)
        app_height = int(SCREEN_HEIGHT * 0.75)

        self.title("QR-Code Anwendung GSG Schulbibliothek")
        self.geometry(f"{app_width}x{app_height}")
        self.resizable(False, False)
        self.iconbitmap("app_icon_white.ico")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Module initialisieren
        self.ui_elements = UIElements(self)
        self.qr_generator = QRGenerator(self.ui_elements)
        self.qr_scanner = QRScanner(self.ui_elements)

        # UI erstellen und Funktionen verbinden
        self.ui_elements.create_ui(self.generate_qr_code, self.save_qr_code, self.upload_qr_image)


    def generate_qr_code(self):
        self.qr_generator.generate_qr_code()

    def save_qr_code(self):
        self.qr_generator.save_qr_code()

    def upload_qr_image(self):
        self.qr_scanner.upload_qr_image()

# QRCodeApp Objekt
app = QRCodeApp()
app.mainloop()
