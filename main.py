from config import *
from tkinter import *
from timers import SessionTimer, ClearingTimer
from dangerous_writing_prompt_ui import DangerousWritingPromptUI


window = Tk()
ui = DangerousWritingPromptUI(window)
session_timer = SessionTimer(
    window, ui.update_session_timer, ui.disable_text_box, ui.display_times_up
)
clearing_timer = ClearingTimer(
    window, ui.update_clearing_timer, ui.clear_textbox, ui.display_word_count
)


def start_timers(_event=None):
    window.unbind("<Key>")
    window.bind("<Key>", clearing_timer.start)
    session_timer.start()
    clearing_timer.start()


window.bind("<Key>", start_timers)


window.mainloop()
