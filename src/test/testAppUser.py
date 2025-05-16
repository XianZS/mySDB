import os
import sys

sys.path.append(os.getcwd())
from src.config import sqlsdObj
from src.config import cuObj
from src.config import wuObj


def main():
    # 1.测试设置数据库存储路径
    sqlsdObj.setNewWorkDir(".")
    # 2.设置数据库名称
    sqlsdObj.setNewFolder("database")
    # 3.创建数据库
    sqlsdObj.enter()
    # 4.检查是否存在XianZS用户,因为XianZS用户肯定不存在，所以需要try-except一下
    judgement, _ = wuObj.enter("XianZS_1")
    if not judgement:
        print("//////////")
        cuObj.enter("XianZS_1")


if __name__ == "__main__":
    main()
