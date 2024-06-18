import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Notas Finall")
        self.geometry("600x400")
        self.resizable(False, False)
        
        self.mainloop()
if __name__ == "__main__":
    root = ctk.CTk()
    MainWindow(root)