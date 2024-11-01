import customtkinter as ctk


class UIElements:
    def __init__(self, window):
        self.window = window
        self.info_frame = None
        self.vorschau_frame = None
        self.qr_label = None
        self.save_button = None
        self.upload_button = None
        self.result_label = None
        self.uploaded_qr_label = None
        self.analyse_result = None

    def create_ui(self, generate_qr_code_callback, save_qr_code_callback, upload_qr_image_callback):
        # App-Grid-Konfiguration
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        # Frame für QR-Code-Erzeugung
        self.info_frame = ctk.CTkFrame(self.window, corner_radius=10, border_width=2, border_color="gray")
        self.info_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.columnconfigure(1, weight=1)
        self.info_frame.columnconfigure(2, weight=1)

        self.info_frame.rowconfigure(0, weight=1)
        self.info_frame.rowconfigure(1, weight=1)
        self.info_frame.rowconfigure(2, weight=1)
        self.info_frame.rowconfigure(3, weight=1)
        self.info_frame.rowconfigure(4, weight=1)


        # "Buchinformationen eingeben" Frame Titel
        label_frame_title = ctk.CTkLabel(self.info_frame, text="Buchinformationen eingeben", font=("Arial", 16, "bold"), anchor="w")
        label_frame_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # Eingabefelder und deren Anordnung
        self.entry_titel = ctk.CTkEntry(self.info_frame, placeholder_text="Titel*")
        self.entry_titel.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.entry_author = ctk.CTkEntry(self.info_frame, placeholder_text="Autor*")
        self.entry_author.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.entry_untertitel = ctk.CTkEntry(self.info_frame, placeholder_text="Untertitel")
        self.entry_untertitel.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.entry_verlag = ctk.CTkEntry(self.info_frame, placeholder_text="Verlag*")
        self.entry_verlag.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.entry_auflage = ctk.CTkEntry(self.info_frame, placeholder_text="Auflage")
        self.entry_auflage.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.entry_jahr = ctk.CTkEntry(self.info_frame, placeholder_text="Jahr")
        self.entry_jahr.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

        self.entry_kategorie = ctk.CTkEntry(self.info_frame, placeholder_text="Kategorie")
        self.entry_kategorie.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.entry_anzahl = ctk.CTkEntry(self.info_frame, placeholder_text="Anzahl")
        self.entry_anzahl.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Schalter für Test Daten
        self.lorem_ipsum_switch = ctk.CTkSwitch(self.info_frame, text="", command=self.test_daten)
        self.lorem_ipsum_switch.grid(row=0, column=2, columnspan=3, padx=10, pady=10, sticky="e")

        # Button zum Erzeugen des QR-Codes
        generate_button = ctk.CTkButton(self.info_frame, text="QR-Code erzeugen", command=generate_qr_code_callback)
        generate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Vorschau-Frame für QR-Code-Anzeige
        self.vorschau_frame = ctk.CTkFrame(self.window)
        self.vorschau_frame.grid(row=0, column=2, columnspan=1, rowspan=2, padx=20, pady=20, sticky="nsew")

        # Vorschau-Frame Grid-Konfiguration
        self.vorschau_frame.grid_rowconfigure(0, weight=1)
        self.vorschau_frame.grid_columnconfigure(0, weight=1)

        # Platzhalter für den QR-Code
        self.qr_label = ctk.CTkLabel(self.vorschau_frame, text="Hier wird der QR-Code angezeigt")
        self.qr_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # "Speichern"-Button
        self.save_button = ctk.CTkButton(self.vorschau_frame, text="Speichern", command=save_qr_code_callback, state="disabled")
        self.save_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Upload-Frame für QR-Code-Scannen
        upload_frame = ctk.CTkFrame(self.window)
        upload_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        upload_frame.grid_rowconfigure(0, weight=1)
        upload_frame.grid_columnconfigure(0, weight=1)

        # Label für die Anzeige des hochgeladenen QR-Codes
        self.uploaded_qr_label = ctk.CTkLabel(upload_frame, text="Kein QR-Code hochgeladen")
        self.uploaded_qr_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # "QR-Code Bild hochladen"-Button
        self.upload_button = ctk.CTkButton(upload_frame, text="QR-Code Bild hochladen",
                                           command=upload_qr_image_callback)
        self.upload_button.grid(row=1, column=0, padx=50, pady=10, sticky="SEW")

        # Frame für Upload-QR-Code-Info
        analyse_result = ctk.CTkFrame(self.window)
        analyse_result.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Ergebnis Label
        self.result_label = ctk.CTkLabel(analyse_result, text="", anchor="w")
        self.result_label.grid(row=0, column=0, padx=20, pady=20)

    def test_daten(self):  # Funktion für Testdateneingabe
        lorem_ipsum_daten = {
            "titel": "Lorem Ipsum",
            "author": "Dolor Sit Amet",
            "verlag": "Sed Do Eiusmod"
        }

        if self.lorem_ipsum_switch.get():  # Wenn der Schalter aktiv ist
            self.entry_titel.delete(0, ctk.END)
            self.entry_titel.insert(0, lorem_ipsum_daten["titel"])
            self.entry_author.delete(0, ctk.END)
            self.entry_author.insert(0, lorem_ipsum_daten["author"])
            self.entry_verlag.delete(0, ctk.END)
            self.entry_verlag.insert(0, lorem_ipsum_daten["verlag"])
        else:  # Wenn der Schalter deaktiviert ist
            self.entry_titel.delete(0, ctk.END)
            self.entry_author.delete(0, ctk.END)
            self.entry_verlag.delete(0, ctk.END)
