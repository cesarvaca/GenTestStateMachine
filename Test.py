# Test

from State import State
from StateMachine import StateMachine

# A different subclass for each state:

class Waiting(State):
    def run(self):
        print("Waiting")

    def next(self, input):
        if input ==



class Test(State):
    def run(self):
        assert 0, "run not implemented"

    def next(self, input):
        if input ==

class Controller(StateMachine):
