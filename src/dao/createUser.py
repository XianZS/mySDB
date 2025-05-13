import os
import sys

sys.path.append(os.getcwd())
from abc import ABC, abstractmethod
from src.config import sqlSD


class IEnter(ABC):
    @abstractmethod
    def enter(self):
        """enter"""


class ICUser(ABC):
    @abstractmethod
    def createUser(self):
        """Create user"""


class CreateUser(IEnter, ICUser):
    def __init__(self):
        self.__road = sqlSD.getRoad()
        self.__userName = "default"

    def __judge(self) -> bool:
        """
        ## 判断User是否已存在
        ## 规则
        * 先获取User:list
        * 再判断当前是否userName是否存在
        * 如果存在返回False，代表用户已存在，不可以二次创建，输出“用户已存在”
        * 如果不存在返回True，代表用户不存在，可以创建该用户，输出“用户不存在”
        ## 返回值
        * bool
        """
        print("i" * 30)
        print(self.__road)
        dirs: list = os.listdir(sqlSD.getRoad())
        if self.__userName in dirs:
            print(f"{self.__userName}已存在，不可以二次创建")
            return False
        print(f"{self.__userName}不存在，正在创建该用户中(^*^)")
        return True

    def createUser(self) -> bool:
        if self.__judge():
            # 以防万一,哈哈，\(*^*)/
            try:
                # 选中当前数据库路径
                os.chdir(sqlSD.getRoad())
                # 创建当前用户文件夹
                os.makedirs(self.__userName)
                return True
            except Exception as e:
                print("____________")
                print(e)
                print("____________")
                return False
        return False

    def enter(self, userName: str):
        self.__userName = userName
        self.createUser()
