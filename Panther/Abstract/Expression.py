from Environment.Symbol import Symbol
from abc import ABC, abstractclassmethod
from Environment.Environment import Environment

class Expression(ABC):

    @abstractclassmethod
    def execute(self, environment: Environment) -> Symbol:
        pass