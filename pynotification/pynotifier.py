"""Module to trigger OS agnostic notifications."""

import logging
import os
from typing import AnyStr, NoReturn, Union

from . import mod, window


def default_logger() -> logging.Logger:
    """Configure default logger.

    Returns:
        Logger:
        Returns the ``Logger`` object as an argument.
    """
    handler = logging.StreamHandler()
    handler.setFormatter(fmt=logging.Formatter(
        datefmt='%b-%d-%Y %I:%M:%S %p',
        fmt='%(asctime)s - %(levelname)s - [%(module)s:%(lineno)d] - %(funcName)s - %(message)s')
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)
    logger.addHandler(hdlr=handler)
    return logger


# noinspection PyProtectedMember
def pynotifier(title: AnyStr, message: AnyStr, dialog: bool = False, icon: Union[str, os.PathLike] = None,
               debug: bool = False, logger: logging.Logger = None, destroy: bool = False) -> NoReturn:
    """Triggers a system notification.

    Args:
        title: Title for the notification.
        message: Message that has to go in the notification window.
        dialog: Boolean value to show a dialog window. Note that this will block the process.
        icon: Add a custom icon for Linux or Windows OS.
        debug: Boolean value to show output logs.
        logger: Bring your own logger for custom logging.
        destroy: Destroy notification balloon immediately on Windows OS.

    See Also:
        - Personalized icons for `Linux OS <https://wiki.ubuntu.com/Artwork/BreatheIconSet/Icons>`__
        - Both Linux and Windows OS support custom icon file for notifications.
        - ``.png`` for Linux
        - ``.ico`` for Windows

    Warnings:
        - Please note that using this module doesn't guarantee a pop-up notification.
        - This module uses built-in tools to trigger a notification.
        - How the notification is displayed solely relies on the system settings.
    """
    if not logger:
        logger = default_logger()
    dialog_box = window.DialogWindow(title=title, message=message, debug=debug, logger=logger)
    if mod._SYSTEM == "Darwin":
        if dialog and dialog_box.mac_dialog():
            return
        result = os.system("""osascript -e 'display notification "%s" with title "%s"'""" % (message, title))
        if debug is False:
            return
        if result == 0:
            logger.info("Notification was successful.")
        else:
            logger.error("Failed to send a notification. Code: %s" % result)
    elif mod._SYSTEM == "Windows":
        if dialog and dialog_box.win_dialog():
            return
        result = mod.WindowsBalloonTip(msg=message, title=title, debug=debug, logger=logger,
                                       icon=icon, destroy=destroy).notify()
        if debug is False:
            return
        if result is True:
            logger.info("Notification was successful.")
        else:
            logger.error(result)
    elif mod._SYSTEM == "Linux":
        if dialog and dialog_box.lin_dialog():
            return
        cmd = "notify-send -t 0 '%s' '%s'" % (title, message)
        if icon:
            cmd += " -i %s" % icon
        result = os.system(cmd)
        if debug is False:
            return
        if result == 0:
            logger.info("Notification was successful.")
        else:
            logger.error("Failed to send a notification. Code: %s" % result)
    else:
        logger.warning("This module is not intended for '%s'" % mod._SYSTEM)
