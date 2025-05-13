import os
import sys

sys.path.append(os.getcwd())
from src.dao.withUser import WithUser as _WithUser
from src.dao.createUser import CreateUser as _CreateUser

withUser = _WithUser()
createUser = _CreateUser()
