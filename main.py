from tkinter import Tk
from timers import SessionTimer, ClearingTimer
from dangerous_writing_prompt_ui import DangerousWritingPromptUI


window = Tk()
ui = DangerousWritingPromptUI(window)
session_timer = SessionTimer(
    window, ui.update_timer_display, ui.disable_text_box, ui.display_times_up
)
clearing_timer = ClearingTimer(window, ui.update_timer_display, ui.clear_textbox)


def start_timers(_event=None):
    window.unbind("<Key>")
    window.bind("<Key>", clearing_timer.start)
    window.bind("<space>", ui.update_word_count)
    session_timer.start()
    clearing_timer.start()


window.bind("<Key>", start_timers)


window.mainloop()
