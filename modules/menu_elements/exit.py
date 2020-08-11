"""
Action class that implements the menu option: EXIT
"""
import os

GOODBYE_MESSAGE = "Goodbye!"


class Exit:
    def __init__(self):
        self.exit_code = 0

    def perform_the_action(self, killMe=True):
        print(GOODBYE_MESSAGE)
        if killMe:
            os._exit(0)
