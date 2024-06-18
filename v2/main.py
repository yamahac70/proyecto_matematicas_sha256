import customtkinter as ctk
from gui.inicio import InicioUi

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Notas Finall")
        self.geometry("600x400")
        self.resizable(False, False)
        
        # Botón para abrir la ventana de inicio
        open_button = ctk.CTkButton(self, text="Abrir Inicio", command=self.open_inicio)
        open_button.pack(pady=20)
        
    def open_inicio(self):
        self.destroy()
        inicio_ui = InicioUi()
        inicio_ui.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()