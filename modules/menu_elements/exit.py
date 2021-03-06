"""
Action class that implements the menu option: EXIT
"""
import os


class Exit:
    def __init__(self):
        self.exit_code = 0
        self.GOODBYE_MESSAGE = "Goodbye!"

    def perform_the_action(self):
        print(self.GOODBYE_MESSAGE)
        os._exit(0)
