import customtkinter as ctk
from gui.inicio import InicioGui
from gui.cifrar.cifrar import CifrarGui
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sha 256")
        self.geometry("600x400")
        self.resizable(False, False)
        
        
        #frames contenedor para las paginas 
        self.container=ctk.CTkFrame(self)
        self.container.place(
            relx=0, rely=0, relwidth=500, relheight=1
        )
        
        self.paginas={}
        self.crearPaginas()
        self.mostrarPagina("Inicio")

    def crearPaginas(self):
        self.paginas["Inicio"] = InicioGui(parent=self.container, controller=self)
        self.paginas["Cifrar"] = CifrarGui(parent=self.container, controller=self)
        for pagina in self.paginas.values():
            pagina.place(relx=0, rely=0, relwidth=1, relheight=1)
    def mostrarPagina(self, pagina,titulo="Sha 256"):
        self.title(titulo)
        pagina=self.paginas[pagina]
        pagina.tkraise()
        
if __name__ == "__main__":
    app = App()
    app.mainloop()