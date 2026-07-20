from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, name):

        self.name = name

    @abstractmethod
    def can_handle(self, request):

        pass

    @abstractmethod
    def execute(self, request):

        pass