import os
import sys
import time


def main() -> bool:
    try:
        print("正在初始化......")
        time.sleep(3)
        sys.path.append(os.getcwd())
        return True
    except Exception as e:
        print(e)
        return False


main()
