from tkinter import filedialog
import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk

class QRScanner:
    def __init__(self, ui_elements):
        self.ui_elements = ui_elements

    # QR-Code Bild hochladen
    def upload_qr_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.display_uploaded_image(file_path)  # Zeigt das hochgeladene Bild an
            self.scan_qr_code(file_path)

    def display_uploaded_image(self, file_path):
        # Bild öffnen und auf die passende Größe skalieren
        image = Image.open(file_path)
        image = image.resize((200, 200))  # Bildgröße für die Anzeige im UI anpassen
        self.uploaded_image = ImageTk.PhotoImage(image)  # In Tkinter-kompatibles Format konvertieren

        # Bild im Label anzeigen und Text entfernen
        self.ui_elements.uploaded_qr_label.configure(image=self.uploaded_image, text="")  # Text entfernen
        self.ui_elements.uploaded_qr_label.image = self.uploaded_image  # Referenz speichern

    # QR-Code scannen und Daten extrahieren
    def scan_qr_code(self, file_path):
        image = cv2.imread(file_path)
        decoded_objects = decode(image)

        if decoded_objects:
            decoded_data = decoded_objects[0].data.decode("utf-8")
            self.ui_elements.result_label.configure(text=f"QR-Code Inhalt: {decoded_data}")
        else:
            self.ui_elements.result_label.configure(text="Kein QR-Code gefunden oder ungültig", anchor="center")



