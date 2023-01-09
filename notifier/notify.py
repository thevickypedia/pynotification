"""Module to trigger OS agnostic notifications."""

import logging
import os
from typing import AnyStr, NoReturn, Optional

from . import mod


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
def notify(title: AnyStr, message: AnyStr, debug: bool = False,
           logger: Optional[logging.Logger] = None) -> NoReturn:
    """Triggers a system notification.

    Args:
        title: Title for the notification.
        message: Message that has to go in the notification window.
        debug: Boolean value to show output logs.
        logger: BYOL (bring your own logger method) to log in any defined fashion.

    See Also:
        - Please note that using this module doesn't guarantee a pop-up notification.
        - This module uses built-in tools to trigger a notification.
        - How the notification is displayed solely relies on the system settings.
    """
    if mod._SYSTEM == "Darwin":
        result = os.system("""osascript -e 'display notification "%s" with title "%s"'""" % (title, message))
        if debug is False:
            return
        if result == 0:
            logger.info("Notification was successful.")
        else:
            logger.error("Failed to send a notification. Code: %s" % result)
    elif mod._SYSTEM == "Windows":
        result = mod.WindowsBalloonTip(msg=message, title=title).notify()
        if debug is False:
            return
        if result is True:
            logger.info("Notification was successful.")
        else:
            logger.error(result)
    elif mod._SYSTEM == "Linux":
        result = os.system("""notify-send -t 0 '%s' '%s'""" % (title, message))
        if debug is False:
            return
        if result == 0:
            logger.info("Notification was successful.")
        else:
            logger.error("Failed to send a notification. Code: %s" % result)
    else:
        logger.warning("This module is not intended for '%s'" % mod._SYSTEM)
