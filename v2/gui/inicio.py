import customtkinter as ctk


class InicioGui(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.controller.title("Sha 256")
        label = ctk.CTkLabel(self, text="Página de Inicio")
        label.grid(row=0, column=0, padx=20, pady=20)

        cifrar_button = ctk.CTkButton(self, text="Ir a Cifrar", command=lambda: controller.mostrarPagina("Cifrar","Cifrar sha 256"))
        cifrar_button.grid(row=1, column=0, padx=20, pady=10)
        
        btnDesifrar = ctk.CTkButton(self, text="Ir a Desifrar", command=lambda: controller.mostrarPagina("Desifrar"))
        btnDesifrar.grid(row=2, column=0, padx=20, pady=10)

        #desifrar_button = ctk.CTkButton(self, text="Ir a Desifrar", command=lambda: controller.show_page("DesifrarPage"))
        #desifrar_button.grid(row=2, column=0, padx=20, pady=10)