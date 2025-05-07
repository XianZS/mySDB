import os
import sys
from pathlib import Path
from abc import ABC,abstractmethod

class ISqlSD(ABC):
    
    @abstractmethod
    def judgeDir(self):
        """
            判断当前目录是否存在
        """
    pass

    @abstractmethod
    def getWorkDir(self):
        """
            获取当前工作的根目录
        """
    pass

class SqlSD(ISqlSD):

    def __init__(self):
        """ init things """
        self.__workDir=os.getcwd()
        self.__folder="databases"

    def judgeDir(self) -> bool:
        return True

    def getWorkDir(self):
        return self.__workDir
    
    def __setWordDir(self,newWordDir:str) -> None:
        self.__workDir=newWordDir
        return True
    
    def createDir(self) -> None:
        os.chdir(self.getWorkDir())
        print(self.getWorkDir())
        os.makedirs(self.__folder)
        return None



if __name__=="__main__":
    sqlSD=SqlSD()
    sqlSD.createDir()