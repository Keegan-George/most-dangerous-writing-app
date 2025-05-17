from tkinter import Tk
from config import SESSION_DURATION, CLEARING_DURATION


class SessionTimer:
    """
    Class to manage the main session timer.
    """

    def __init__(
        self,
        root: Tk,
        update_session_timer_callback,
        disable_textbox_callback,
        times_up_callback,
    ):
        self.root = root
        self.after_id = None
        self.duration = SESSION_DURATION
        self.update_session_timer_callback = update_session_timer_callback
        self.disable_textbox_callback = disable_textbox_callback
        self.times_up_callback = times_up_callback

    def tick(self):
        if self.duration < 0:
            self.root.after_cancel(self.after_id)
            self.disable_textbox_callback()
            self.times_up_callback()

        else:
            self.minutes = self.duration // 60
            self.seconds = self.duration % 60
            self.update_session_timer_callback(self.minutes, self.seconds)
            self.duration -= 1
            self.after_id = self.root.after(1000, self.tick)

    def start(self):
        """
        Start timer. 
        """
        self.tick()


class ClearingTimer:
    """
    Class to manage the clearing timer.
    """

    def __init__(
        self,
        root: Tk,
        update_clearing_timer_callback,
        clearing_textbox_callback,
        update_word_count_callback,
    ):
        self.root = root
        self.after_id = None
        self.duration = CLEARING_DURATION
        self.update_clearing_timer_callback = update_clearing_timer_callback
        self.clearing_textbox_callback = clearing_textbox_callback
        self.update_word_count_callback = update_word_count_callback

    def tick(self):
        if self.duration < 0:
            self.clearing_textbox_callback()
            self.root.after_cancel(self.after_id)

        else:
            self.minutes = self.duration // 60
            self.seconds = self.duration % 60
            self.update_clearing_timer_callback(self.minutes, self.seconds)
            self.duration -= 1
            self.after_id = self.root.after(1000, self.tick)

    def start(self, _event=None):
        """
        Start timer. Cancels an existing timer if one is running. 
        """
        self.duration = CLEARING_DURATION
        if self.after_id:
            self.root.after_cancel(self.after_id)
        self.tick()
