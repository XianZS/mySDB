import sqlStorageDir


def main():
    """main function"""
    sqlSD = sqlStorageDir.SqlSD()
    sqlSD.setNewWorkDir("C:/Users/Administrator/Desktop")
    sqlSD.setNewFolder("XianZS")
    sqlSD.enter()


if __name__ == "__main__":
    main()
