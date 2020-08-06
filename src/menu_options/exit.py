"""
Action class that implements the menu option: EXIT
"""
import os


class Exit:
    def __init__(self):
        self.exit_code = 0

    def perform_the_action(self):
        print("goodbye")
        os._exit(0)
