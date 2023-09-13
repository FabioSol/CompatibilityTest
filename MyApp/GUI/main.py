import customtkinter
from MyApp.Backend.get_text import get_text_from_db

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
counter=1
class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=1, padx=20, pady=20, sticky="nsew", rowspan=3, columnspan=3)


class TestFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global counter
        self.grid(row=0, column=1, padx=20, pady=20, sticky="nsew", rowspan=3, columnspan=3)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(0, minsize=0)
        self.grid_rowconfigure((1, 2), weight=1)
        self.test_label = customtkinter.CTkLabel(self,text=get_text_from_db()+f" {counter}")
        counter+=1
        self.test_label.grid(row=0,column=1)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Compatibility Test.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Compatibility Test",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_input_button_event,text="Click to Test")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        self.my_frame = MainFrame(master=self)
        self.my_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew", rowspan=3, columnspan=3)

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def sidebar_input_button_event(self):
        self.my_frame = TestFrame(master=self)



if __name__ == "__main__":
    app = App()
    app.mainloop()
