class FakeExit:
    def __init__(self):
        self.exit_code = 0
        self.GOODBYE_MESSAGE = "Goodbye!"

    def perform_the_action(self):
        print(self.GOODBYE_MESSAGE)
