# noinspection PyUnresolvedReferences
"""Module to trigger notifications in WindowsOS, using windows binaries for API and GUI.

>>> WindowsNotifications

"""

import os
import pathlib
import platform
import time
from typing import NoReturn, Union

_SYSTEM = platform.system()

if _SYSTEM == "Windows":
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    import win32api
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    import win32con
    # noinspection PyUnresolvedReferences,PyPackageRequirements
    import win32gui


class WindowsBalloonTip:
    """Instantiates WindowsBalloonTip object as a dedicated process to trigger notification in Windows OS.

    >>> WindowsBalloonTip

    """

    def __init__(self, title: str, msg: str, destroy: bool = False):
        """Initialize the object and assign create members for arguments received.

        Args:
            title: Title of the notification.
            msg: Message for the notification.
            destroy: Destroy notification balloon immediately.
        """
        self.title = title
        self.msg = msg
        self.destroy = destroy
        self.hwnd: int = 0

    def run(self) -> NoReturn:
        """Create a window class and sends a notification."""
        message_map = {
            win32con.WM_DESTROY: self.on_destroy,
        }

        # Register the Window class
        window = win32gui.WNDCLASS()
        h_instance = window.hInstance = win32api.GetModuleHandle(None)
        window.lpszClassName = "PythonTaskbar"
        window.lpfnWndProc = message_map  # could also specify a wndproc.
        class_atom = win32gui.RegisterClass(window)

        # Create the Window
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(class_atom, "Taskbar", style, 0, 0, win32con.CW_USEDEFAULT,
                                          win32con.CW_USEDEFAULT, 0, 0, h_instance, None)

        # Update the Window
        win32gui.UpdateWindow(self.hwnd)
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        icon_path_name = os.path.join(pathlib.Path(__file__).parent, "notification.ico")
        if os.path.isfile(icon_path_name):
            hicon = win32gui.LoadImage(h_instance, icon_path_name, win32con.IMAGE_ICON, 0, 0, icon_flags)
        else:
            hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, (self.hwnd, 0, win32gui.NIF_INFO, win32con.WM_USER + 20,
                                                        hicon, "Balloon  tooltip", self.msg, 200, self.title))
        if self.destroy:
            time.sleep(0.5)
            win32gui.DestroyWindow(self.hwnd)

    def notify(self) -> Union[bool, str]:
        """Run notification as balloon window tip.

        Returns:
            Union[bool, str]:
            Returns a boolean flag if notification was successful, otherwise the error string.
        """
        try:
            self.run()
            return True
        except Exception as error:
            return error.__str__()

    def on_destroy(self, *args, **kwargs) -> NoReturn:
        """Destroys the notification window created.

        Args:
            *args: Arguments.
            **kwargs: Keyword arguments.

        Keyword Args:
            hwnd, msg, wparam, lparam
        """
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32api.PostQuitMessage(0)  # Terminate the app.
