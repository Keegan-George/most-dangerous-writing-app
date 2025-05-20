from tkinter import Tk
from config import SESSION_DURATION, CLEARING_DURATION


class BaseTimer:
    """
    Base timer class.
    """

    def __init__(self, root: Tk, update_timer_display_callback):
        self.root = root
        self.update_timer_display_callback = update_timer_display_callback
        self.after_id = None
        self.duration = None
        self.timer_type = None

    def tick(self):
        """
        Decrement the current time by 1 second on each call. 
        """
        if self.duration < 0:
            self.stop()

        else:
            self.minutes = self.duration // 60
            self.seconds = self.duration % 60
            self.update_timer_display_callback(
                self.timer_type, self.minutes, self.seconds
            )
            self.duration -= 1
            self.after_id = self.root.after(1000, self.tick)

    def start(self):
        self.tick()

    def stop(self):
        self.root.after_cancel(self.after_id)


class SessionTimer(BaseTimer):
    """
    Class to manage the main session timer.
    """

    def __init__(
        self,
        root: Tk,
        update_timer_display_callback,
        disable_textbox_callback,
        times_up_callback,
    ):
        super().__init__(root, update_timer_display_callback)
        self.disable_textbox_callback = disable_textbox_callback
        self.times_up_callback = times_up_callback
        self.duration = SESSION_DURATION
        self.timer_type = "s"

    def tick(self):
        if self.duration < 0:
            self.disable_textbox_callback()
            self.times_up_callback()

        super().tick()


class ClearingTimer(BaseTimer):
    """
    Class to manage the clearing timer.
    """

    def __init__(
        self,
        root: Tk,
        update_timer_display_callback,
        clearing_textbox_callback,
    ):
        super().__init__(root, update_timer_display_callback)
        self.clearing_textbox_callback = clearing_textbox_callback
        self.timer_type = "c"

    def tick(self):
        if self.duration < 0:
            self.clearing_textbox_callback()

        super().tick()


    def start(self, _event=None):
        """
        Start clearing timer. Cancels an existing timer if one is running.
        """
        self.duration = CLEARING_DURATION
        if self.after_id:
            self.root.after_cancel(self.after_id)
        super().tick()
