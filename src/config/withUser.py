import os
import sys

sys.path.append(os.getcwd())
from abc import ABC, abstractmethod
from .sqlStorageDir import sqlsdObj


class IEnter(ABC):
    @abstractmethod
    def enter(self):
        """enter"""


class IJudgement(ABC):
    @abstractmethod
    def jUser(self, userName: str) -> bool:
        """
        ## Function:
        The function of this function is to determine whether the user already exists.
        ## Return:
        if not exists:
        &emsp;return False
        else:
        &emsp;return True
        """
        return True


class IWithUser(ABC):

    @abstractmethod
    def revisePermission(self, userName: str) -> bool:
        """That function is revise permission."""

    @abstractmethod
    def enter(self) -> bool:
        """enter class"""


class WithUser(IJudgement, IWithUser, IEnter):
    """
    ## Function:
    先判断用户是否已经存在,如果存在就继续创建，否则报错
    """

    def __init__(self):
        self.__user = "default"

    def jUser(self, userName: str):
        print(sqlsdObj.getRoad())
        dirs: list = os.listdir(sqlsdObj.getRoad())
        if userName in dirs:
            return True
        return False

    def revisePermission(self, userName):
        pass

    def enter(self, userName: str) -> tuple:
        if self.jUser(userName=userName):
            self.__user = userName
            return (True, userName)
        else:
            print("ERROR: User does not exist, please create a user first.")
            return (False, userName)


wuObj = WithUser()

if __name__ == "__main__":
    withUser = WithUser()
    print(withUser.enter("userName"))
