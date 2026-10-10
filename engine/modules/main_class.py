from .sherlock import Sherlock

class Main:
    def __init__ (self, username):
        self.username = username

    def execute_all(self):
        self.sherlock()

    def sherlock(self):
        sherlock = Sherlock()
        return sherlock.execute(self.username)
        