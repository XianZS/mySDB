import os
import sys

sys.path.append(os.getcwd())
from src.config import sqlSD
from src.dao import createUser
from src.dao import withUser


def main():
    # 1.测试设置数据库存储路径
    sqlSD.setNewWorkDir(".")
    # 2.设置数据库名称
    sqlSD.setNewFolder("database")
    # 3.创建数据库
    sqlSD.enter()
    # 4.检查是否存在XianZS用户,因为XianZS用户肯定不存在，所以需要try-except一下
    judgement, _ = withUser.enter("XianZS")
    if not judgement:
        print("//////////")
        createUser.enter("XianZS")


if __name__ == "__main__":
    main()
