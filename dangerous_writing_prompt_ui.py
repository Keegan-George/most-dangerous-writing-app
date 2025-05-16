from tkinter import *
from config import *


class DangerousWritingPromptUI:
    """
    Class to create and update the Dangerous Writing Prompt UI
    """

    def __init__(self, root: Tk):
        self.root = root
        self.root.title(TITLE)
        self.root.config(padx=PADX, pady=PADY, bg=WINDOW_COLOUR)
        self.root.geometry(WINDOW_RESOLUTION)

        # textbox
        self.textbox = Text(width=65)
        self.textbox.configure(
            font=FONT,
            borderwidth=0,
            bg=TEXTBOX_COLOUR,
            fg=TEXT_COLOUR,
        )
        self.textbox.grid(row=1, column=0, columnspan=2)
        self.textbox.focus()

        # session timer display
        self.session_timer_label = Label(
            text=f"Session timer: 00:00", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR
        )
        self.session_timer_label.grid(row=0, column=1)

        # clearing timer display
        self.clearing_timer_label = Label(
            text=f"Clearing timer: 00:00", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR
        )
        self.clearing_timer_label.grid(row=0, column=0)

        # time up message
        self.times_up_label = Label(font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR)
        self.times_up_label.grid(row=2, column=0, columnspan=2)

        # word count display
        self.word_count_label = Label(
            text=f"Word count: 0", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR
        )
        self.word_count_label.grid(row=3, column=0, columnspan=2)
