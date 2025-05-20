from config import *
from tkinter import *


class DangerousWritingAppUI:
    """
    Class to create and update the Dangerous Writing Prompt UI
    """

    def __init__(self, root: Tk):
        self.root = root
        self.root.title(TITLE)
        self.root.config(padx=PADX, pady=PADY, bg=WINDOW_COLOUR)
        self.root.geometry(WINDOW_RESOLUTION)

        # textbox
        self.textbox = Text(width=TEXTBOX_WIDTH)
        self.textbox.configure(
            font=FONT,
            borderwidth=0,
            bg=TEXTBOX_COLOUR,
            fg=FONT_COLOUR,
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

        # times up message
        self.times_up_label = Label(font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR)
        self.times_up_label.grid(row=2, column=0, columnspan=2)

        # word count display
        self.word_count_label = Label(
            text=f"Word count: 0", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR
        )
        self.word_count_label.grid(row=3, column=0, columnspan=2)

    def update_timer_display(self, timer_type: str, minutes: int, seconds: int):
        """
        Update the selected timer with the provided time in minutes:seconds.

        Set timer_type to 's' or 'c' to update the display for the "session" or "clearing" timer accordingly.

        """
        if not timer_type in ("s", "c"):
            raise ValueError

        if timer_type == "s":
            self.session_timer_label.config(
                text=f"Session timer: {minutes:02d}:{seconds:02d}"
            )
        if timer_type == "c":
            self.clearing_timer_label.config(
                text=f"Clearing timer: {minutes:02d}:{seconds:02d}"
            )

    def disable_text_box(self):
        """
        Disable the input textbox.
        """
        self.textbox.config(state="disabled")

    def display_times_up(self):
        """
        Display "Times Up" message.
        """
        self.times_up_label.config(text="Times Up!")

    def update_word_count(self, _event=None):
        """
        Display the number of words typed.
        """
        words = len(self.textbox.get("1.0", "end").split())
        self.word_count_label.config(text=f"Word count: {words}")

    def clear_textbox(self):
        """
        Clear input textbox.
        """
        self.textbox.delete("1.0", "end")
