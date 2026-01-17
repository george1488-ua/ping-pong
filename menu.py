from customtkinter import *

class GameMenu(CTk):
    def __init__(self):
        super().__init__()

        self.title("Ping Pong")
        self.geometry("300x300")

        self.port = ""
        self.host = 0

        CTkLabel(self, text="Введіть хост і порт").pack(padx=5)

        self.host_entry = CTkEntry(self, placeholder_text="Host")
        self.host_entry.pack(padx=5)

        self.port_entry = CTkEntry(self, placeholder_text="Port")
        self.port_entry.pack(padx=5)

        CTkButton(self, text="Грати", command=self.start_game).pack(padx=5)


    def start_game(self):
        self.host = self.host_entry.get()
        self.port = int(self.port_entry.get())
        self.quit()
        self.destroy()


def get_connection():
    app = GameMenu()
    app.mainloop()
    return app.host, app.port