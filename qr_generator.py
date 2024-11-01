import qrcode
import io
from PIL import Image
import customtkinter as ctk
from tkinter import filedialog

class QRGenerator:
    def __init__(self, ui_elements):
        self.ui_elements = ui_elements
        self.qr_image = None

    # Erstellen des QR Codes mit qrcode
    def generate_qr_code(self):
        titel = self.ui_elements.entry_titel.get()
        author = self.ui_elements.entry_author.get()
        untertitel = self.ui_elements.entry_untertitel.get()
        verlag = self.ui_elements.entry_verlag.get()
        auflage = self.ui_elements.entry_auflage.get()
        jahr = self.ui_elements.entry_jahr.get()
        kategorie = self.ui_elements.entry_kategorie.get()
        anzahl = self.ui_elements.entry_anzahl.get()

        # QR-Code nur generieren, wenn wichtige Felder ausgefüllt sind (als key-value Paar)
        if titel and author and verlag:
            qr_data_raw: dict = {
                "Titel": str(titel),
                "Untertitel": str(untertitel),
                "Author": str(author),
                "Verlag": str(verlag),
                "Edition": str(auflage),
                "Veröffentlicht": str(jahr),
                "Kategorie": str(kategorie),
                "Anzahl" : str(anzahl)
            }
            # Formatierung des Output textes ändern
            qr_data = "\n".join([f"{key}: {value}" for key, value in qr_data_raw.items()])

            qr = qrcode.QRCode(version=None, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_H) # Hohe Error Correction = Toleranz für physische Beschädigung
            qr.add_data(qr_data)
            qr.make(fit=True)

            # Bild im Speicher (BytesIO) speichern für Vorschau ohne lokales Speichern
            img = qr.make_image(fill="black", back_color="white")
            bio = io.BytesIO()
            img.save(bio, format="PNG")
            bio.seek(0)

            # Bild für die Anzeige in Tkinter vorbereiten
            self.qr_image = Image.open(bio)
            ctk_image = ctk.CTkImage(self.qr_image, size=(200, 200))

            # Bild im GUI anzeigen
            self.ui_elements.qr_label.configure(image=ctk_image, text="")  # Text entfernen
            self.ui_elements.qr_label.image = ctk_image

            # "Speichern"-Button aktivieren
            self.ui_elements.save_button.configure(state="normal")

    # Speichern des QR-Codes auf dem System
    def save_qr_code(self):
        if self.qr_image:
            # Vordefinierter Dateiname aus dem Titel des Buches
            title = self.ui_elements.entry_titel.get()
            default_filename = f"{title}.png" if title else "QR_Code.png"

            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png")],
                                                     initialfile=default_filename)
            if file_path:
                self.qr_image.save(file_path)
                print(f"QR-Code gespeichert unter: {file_path}")
