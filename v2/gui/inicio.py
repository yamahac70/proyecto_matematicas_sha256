import customtkinter as ctk

class InicioUi(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inicio")
        self.geometry("600x400")
        self.resizable(False, False)
        # Aquí puedes añadir los widgets y la lógica de la pantalla de inicio
        label = ctk.CTkLabel(self, text="Pantalla de Inicio")
        label.pack(pady=20)

        close_button = ctk.CTkButton(self, text="Cerrar", command=self.close)
        close_button.pack(pady=20)

    def close(self):
        self.destroy()