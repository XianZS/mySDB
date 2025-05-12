import sqlite3
from abc import ABC, abstractmethod


class IOpenDB(ABC):
    @abstractmethod
    def openDB(self, dbName):
        """That open database that named dbName"""


class OpendDB(IOpenDB):
    def openDB(self, dbName):
        sqlite3.connect(dbName)
