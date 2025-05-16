import os
import sys

# sys.path.append(os.getcwd())
from abc import ABC, abstractmethod


class IEnter(ABC):
    @abstractmethod
    def enter(self):
        """enter function"""


class ConnectDB:
    def __init__(self):
        self.name = "kom"


connObj = ConnectDB()
