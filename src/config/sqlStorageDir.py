"""
## Author

> XianZS

## Interface

* ISqlSDPath:interface

## Class

* SqlSD:class

&emsp;&emsp;
"""

import os
import sys
from pathlib import Path
from abc import ABC, abstractmethod


class ISqlSDPath(ABC):

    @abstractmethod
    def setNewWorkDir(self, newWorkDir: str):
        """
        ## 1.Function:
            传入的newWorkDir参数必须实际存在，默认为当前工作目录
            * 设置当前的工作目录
            * 判断相对路径或绝对路径
            * 支持相对路径设置
            * 支持绝对路径设置
        ## 2. Example using:
        ### (1).绝对路径设置
            > C:/user/admin
        ### (2).相对路径设置
            > ./user/admin
        """

    @abstractmethod
    def setNewFolder(self, newFolder: str):
        """
        ## 1. Function:
        &emsp;&emsp;传入参数newFolder可以不存在，默认参数为databases，设置当前数据库名称。
        * 用户存在时，使用
        * 用户不存在时，创建
        ## 2.Example using:
        &emsp;&emsp;假设setNewFolder="XianZS",
        那么就会在sql工作目录下创建一个名为XianZS
        的文件夹,XianZS就是新建用户。
        """

    @abstractmethod
    def getRoad(self):
        """Get Road"""

    @abstractmethod
    def enter(self):
        """创建缓存目录"""


class SqlSD(ISqlSDPath):
    """
    ## Author
        > XianZS
    ## Open method
        * sqlSD.setNewWorkDir(newWorkDir:str),setting working dir that default is now working dir.
        * sqlSD.setNewFolder(newFolder:str),setting newFolder that default is `databases`.
        * sqlSD.enter(),initiate the class.
    """

    _instance = None

    def __init__(self):
        """init things"""
        self.__workDir = os.getcwd()
        self.__folder = "databases"
        self.__createJudgeMent = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SqlSD, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def setNewWorkDir(self, newWorkDir: str):
        self.__workDir = newWorkDir
        pObj = Path(newWorkDir)
        j = pObj.is_absolute()
        if j:
            """绝对路径"""
            self.__workDir = newWorkDir
            print("绝对路径为:", self.__workDir)
        else:
            """相对路径"""
            self.__workDir = newWorkDir
            print("相对路径为:", self.__workDir)

    def setNewFolder(self, newFolder: str) -> bool:
        try:
            self.__folder = newFolder
            return True
        except Exception as e:
            print(e)
            return False

    def getRoad(self):
        return self.__Road()

    def __createDir(self) -> bool:
        """This is a private method."""
        try:
            os.chdir(self.__workDir)
            print(self.__workDir + "/" + self.__folder)
            if os.path.exists(self.__workDir + "/" + self.__folder):
                """pass"""
                print(f"{self.__workDir}/{self.__folder}文件目录存在,不会进行二次创建.")
            else:
                print(f"{self.__workDir}/{self.__folder}文件目录不存在,创建成功.")
                os.makedirs(self.__folder)
            self.__createJudgeMent = True
        except Exception as e:
            print(e)
            self.__createJudgeMent = False
        return self.__createJudgeMent

    def __Road(self):
        print("========")
        print(self.__workDir, self.__folder)
        print("========")
        return self.__workDir + "/" + self.__folder

    def enter(self) -> bool:
        try:
            """try"""
            self.__createDir()
            return True
        except Exception as e:
            print(e)
            return False


sqlsdObj = SqlSD()


if __name__ == "__main__":
    sqlSDFile = SqlSD()
    sqlSDFile.enter()
