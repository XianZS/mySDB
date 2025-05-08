import os
import sys
from pathlib import Path
from abc import ABC, abstractmethod


class ISqlSD(ABC):

    @abstractmethod
    def setNewWorkDir(self, newWorkDir: str):
        """判断当前目录是否存在"""

    @abstractmethod
    def setNewFolder(self, newFolder: str):
        """
        ## 1. Function:
            * 设置当前sql文件存储的路径
            * 支持绝对路径设置
            * 支持相对路径设置
        ## 2. Example using:
        ### (1).绝对路径设置
            > C:/user/admin
        ### (2).相对路径设置
            > ./user/admin
        """

    @abstractmethod
    def createDir(self):
        """創建緩存目錄"""


class SqlSD(ISqlSD):

    def __init__(self):
        """init things"""
        self.__workDir = os.getcwd()
        self.__folder = "databases"
        self.__createJudgeMent = False
        self.createDir()

    def setNewWorkDir(self, newWorkDir):
        """判断相对还是绝对路径"""
        pObj = Path(newWorkDir)
        j = pObj.is_absolute()
        if j:
            """绝对路径"""
            self.__workDir = newWorkDir
        else:
            """相对路径"""
            self.__workDir += newWorkDir

    def __createDir(self) -> None:
        try:
            self.setNewFolder("./")
            os.chdir(self.__workDir)
            # print(self.getWorkDir())
            os.makedirs(self.__folder)
            self.__createJudgeMent = True
        except Exception as e:
            print(e)
            self.__createJudgeMent = False
        return self.__createJudgeMent


if __name__ == "__main__":
    sqlSD = SqlSD()
    sqlSD.createDir()
