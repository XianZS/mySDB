import os
import sys

sys.path.append(os.getcwd())
from src.config import sqlSD


def main():
    """main function"""
    print("""main function""")
    index = 1
    for childPath in sys.path:
        print(f"[{index}]:{childPath}")
        index += 1
    # 绝对路径测试
    # sqlSD.setNewWorkDir("C:/Users/Administrator/Desktop")
    # 相对路径测试
    # sqlSD.setNewWorkDir("src")
    # sqlSD.setNewFolder("XianZS")
    sqlSD.enter()


if __name__ == "__main__":
    main()
