from config import *
from tkinter import *
from dangerous_writing_prompt_ui import DangerousWritingPromptUI


window = Tk()
ui = DangerousWritingPromptUI(window)


session_timer_started = False
session_timer_id = None
clearing_timer_id = None


def session_timer(duration: int):
    """
    function that acts as a timer for the overal writing session

    """
    global session_timer_started, session_timer_id

    # rebinds keys and start clearing timer
    if not session_timer_started:
        session_timer_started = True
        window.unbind("<Key>")
        window.bind("<Key>", lambda event: clearing_timer(CLEARING_DURATION))
        clearing_timer(CLEARING_DURATION)

    # stop session timer
    if duration < 0:
        session_timer_started = False
        window.after_cancel(session_timer_id)
        ui.textbox.config(state="disabled")
        ui.times_up_label.config(text="Times Up!")

    # decrement timer and display on screen
    else:
        minutes = duration // 60
        seconds = duration % 60
        ui.session_timer_label.config(
            text=f"Session timer: {minutes:02d}:{seconds:02d}"
        )
        session_timer_id = window.after(1000, session_timer, duration - 1)


def clearing_timer(duration: int):
    """
    function that clears the text box after a specified amount of time has elapsed
    """
    global clearing_timer_id

    # count and display the number of words typed
    words = len(ui.textbox.get("1.0", "end").split())
    ui.word_count_label.config(text=f"Word count: {words}")

    # restart clearing_timer each time it's run
    if clearing_timer_id:
        window.after_cancel(clearing_timer_id)

    if session_timer_started:
        # clear textbox
        if duration < 0:
            ui.textbox.delete("1.0", "end")
            window.after_cancel(clearing_timer_id)

        else:
            minutes = duration // 60
            seconds = duration % 60
            ui.clearing_timer_label.config(
                text=f"Clearing timer: {minutes:02d}:{seconds:02d}"
            )
            clearing_timer_id = window.after(1000, clearing_timer, duration - 1)


window.bind("<Key>", lambda event: session_timer(SESSION_DURATION))

window.mainloop()
