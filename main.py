from config import *
from tkinter import *


window = Tk()
window.title("Most Dangerous Writing App")
window.config(padx=20, pady=10, bg=WINDOW_COLOUR)
window.geometry(WINDOW_RESOLUTION)
session_timer_started = False
session_timer_id = None
clearing_timer_id = None

# widgets
textbox = Text(width=65)
textbox.configure(
    font=FONT,
    borderwidth=0,
    bg=TEXTBOX_COLOUR,
    fg=TEXT_COLOUR,
)
textbox.focus()
session_timer_label = Label(
    text=f"Session timer: 00:00", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR
)
clearing_timer_label = Label(
    text=f"Clearing timer: 00:00", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR
)
times_up_label = Label(font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR)
word_count_label = Label(text=f"Word count: 0", font=FONT, bg=WINDOW_COLOUR, fg=LABEL_COLOUR)

# widget positions
clearing_timer_label.grid(row=0, column=0)
session_timer_label.grid(row=0, column=1)
textbox.grid(row=1, column=0, columnspan=2)
times_up_label.grid(row=2, column=0, columnspan=2)
word_count_label.grid(row=3, column=0, columnspan=2)



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
        textbox.config(state="disabled")
        times_up_label.config(text="Times Up!")

    # decrement timer and display on screen
    else:
        minutes = duration // 60
        seconds = duration % 60
        session_timer_label.config(text=f"Session timer: {minutes:02d}:{seconds:02d}")
        session_timer_id = window.after(1000, session_timer, duration - 1)


def clearing_timer(duration: int):
    """
    function that clears the text box after a specified amount of time has elapsed
    """
    global clearing_timer_id

    #count and display the number of words typed
    words = len(textbox.get("1.0", "end").split())
    word_count_label.config(text=f"Word count: {words}")

    # restart clearing_timer each time it's run
    if clearing_timer_id:
        window.after_cancel(clearing_timer_id)

    if session_timer_started:
        # clear textbox
        if duration < 0:
            textbox.delete("1.0", "end")
            window.after_cancel(clearing_timer_id)

        else:
            minutes = duration // 60
            seconds = duration % 60
            clearing_timer_label.config(
                text=f"Clearing timer: {minutes:02d}:{seconds:02d}"
            )
            clearing_timer_id = window.after(1000, clearing_timer, duration - 1)



window.bind("<Key>", lambda event: session_timer(SESSION_DURATION))

window.mainloop()
