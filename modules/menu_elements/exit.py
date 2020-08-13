"""
Action class that implements the menu option: EXIT
"""
import os


class Exit:
    def __init__(self):
        self.exit_code = 0
        self.GOODBYE_MESSAGE = "Goodbye!"

    def perform_the_action(self, killMe=True):
        print(self.GOODBYE_MESSAGE)
        if killMe:
            os._exit(0)
