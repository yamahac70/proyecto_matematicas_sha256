from pathlib import Path
from tkinter import Toplevel, Canvas, Entry, Text, Button, PhotoImage

def cifradoUi(parent):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Toplevel(parent)  # Use Toplevel to create a new window
    window.geometry("565x386")
    window.configure(bg="#4E93FC")

    canvas = Canvas(
        window,
        bg="#4D93FB",
        height=319,
        width=565,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    window.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(164.0, 190.0, image=window.image_image_1)

    window.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(436.0, 200.0, image=window.image_image_2)

    window.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=window.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(x=324.0, y=318.0, width=107.0, height=35.0)

    window.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=window.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(x=444.0, y=318.0, width=107.0, height=35.0)

    window.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=window.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(x=108.0, y=210.0, width=107.0, height=35.0)

    window.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=window.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(x=105.0, y=124.0, width=112.0, height=35.0)

    canvas.create_rectangle(25.0, 162.0, 304.0, 205.0, fill="#D9D9D9", outline="")
    canvas.create_text(25.0, 176.0, anchor="nw", text="Ruta", fill="#000000", font=("Inter SemiBold", 12 * -1))
    canvas.create_text(18.0, 39.0, anchor="nw", text="CIFRADO SHA256", fill="#FFFFFF", font=("Inter Bold", 32 * -1))

    window.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(436.0, 181.0, image=window.entry_image_1)
    entry_1 = Text(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_1.place(x=321.0, y=52.0, width=230.0, height=256.0)

    window.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=window.button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(x=491.0, y=361.0, width=56.674713134765625, height=23.999988555908203)

    window.resizable(False, False)