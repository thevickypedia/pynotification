"""Module to trigger notification in a message box."""

import ctypes
import logging
import os
import subprocess
from typing import AnyStr


class DialogWindow:
    """Module to show pop-up dialog window that blocks the process until a button is clicked.

    >>> DialogWindow

    """

    def __init__(self, title: AnyStr, message: AnyStr, debug: bool, logger: logging.Logger):
        """Instantiate all the required args.

        Args:
            title: Title for the notification.
            message: Message that has to go in the notification window.
            debug: Boolean value to show output logs.
            logger: Bring your own logger for custom logging.
        """
        self.title = title
        self.message = message
        self.debug = debug
        self.logger = logger

    def mac_dialog(self) -> bool:
        """Handle dialog window for macOS."""
        appscript = """
        display dialog "{message}" ¬
        with title "{title}" ¬
        with icon caution ¬
        buttons "OK"
        """
        appscript = "osascript -e '%s'" % appscript.format(title=self.title, message=self.message)
        try:
            response = subprocess.check_output(appscript, shell=True)
        except subprocess.SubprocessError as error:
            self.logger.error(error) if self.debug else None
            return False
        response = response.decode(encoding="UTF-8").strip()
        if self.debug:
            if response == "button returned:OK":
                self.logger.info(response)
            else:
                self.logger.error(response)
        return True

    def win_dialog(self) -> bool:
        """Handle dialog window for Windows."""
        try:
            messagebox = ctypes.windll.user32.MessageBoxW
            messagebox(None, self.message, self.title, 0)
            self.logger.info("Popup dialog was successful.") if self.debug else None
        except Exception as error:
            self.logger.error(error) if self.debug else None
            return False
        return True

    def lin_dialog(self) -> bool:
        """Handle dialog window for Linux."""
        result = os.system("zenity --info --title '%s' --text '%s'" % (self.title, self.message))
        if result == 0:
            self.logger.info("Popup dialog was successful.") if self.debug else None
            return True
        else:
            self.logger.error("Failed to show popup dialog. Code: %s" % result) if self.debug else None
