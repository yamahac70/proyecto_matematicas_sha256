import customtkinter

class CifrarGui(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.label = customtkinter.CTkLabel(self, text="Desifrar Page")
        self.label.grid(row=0, column=0, padx=20, pady=20)
        
        self.back_button = customtkinter.CTkButton(self, text="Back to Inicio", 
                                                   command=lambda: self.Inicio() )
        self.back_button.grid(row=1, column=0, padx=20, pady=10)
    def Inicio(self):
        self.controller.mostrarPagina("Inicio","Inicio")
        #self.controller.title("Inicio")