"""
## author

> XianZS

## means

&emsp;&emsp;
"""

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
    def enter(self):
        """創建緩存目錄"""


class SqlSD(ISqlSD):

    def __init__(self):
        """init things"""
        self.__workDir = os.getcwd()
        self.__folder = "databases"
        self.__createJudgeMent = False

    def setNewWorkDir(self, newWorkDir: str):
        """判断相对还是绝对路径"""
        pObj = Path(newWorkDir)
        j = pObj.is_absolute()
        if j:
            """绝对路径"""
            self.__workDir = newWorkDir
            print("绝对路径为:", self.__workDir)
        else:
            """相对路径"""
            self.__workDir += newWorkDir
            print("相对路径为:", self.__workDir)

    def setNewFolder(self, newFolder: str) -> bool:
        """设置NewFolder存储文件夹"""
        try:
            self.__folder = newFolder
            return True
        except Exception as e:
            print(e)
            return False

    def __createDir(self) -> bool:
        try:
            os.chdir(self.__workDir)
            # print(self.getWorkDir())
            print(self.__workDir + "/" + self.__folder)
            if os.path.exists(self.__workDir + "/" + self.__folder):
                """pass"""
                print(f"{self.__workDir}/{self.__folder}文件目录存在,不会进行二次创建.")
            else:
                print(f"{self.__workDir}/{self.__folder}文件目录不存在,创建成功.")
                os.makedirs(self.__folder)
            self.__createJudgeMent = True
        except Exception as e:
            print("----------")
            print(e)
            self.__createJudgeMent = False
        return self.__createJudgeMent

    def enter(self) -> bool:
        try:
            """try"""
            self.__createDir()
            return True
        except Exception as e:
            print(e)
            return False


sqlSD = SqlSD()

if __name__ == "__main__":
    sqlSDFile = SqlSD()
    sqlSDFile.enter()
