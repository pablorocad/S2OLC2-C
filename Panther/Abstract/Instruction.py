from abc import ABC, abstractclassmethod
from Environment.Environment import Environment

class Instruction(ABC):

    @abstractclassmethod
    def execute(self, environment: Environment):
        pass