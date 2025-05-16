import os
import sys

sys.path.append(os.getcwd())
# Format:from .file import class as _class
from src.config.connectDB import connObj as _connObj
from src.config.createUser import cuObj as _cuObj
from src.config.sqlStorageDir import sqlsdObj as _sqlsdObj
from src.config.withUser import wuObj as _wuObj

# Instantiate class objects that enable = _Enable()
connObj = _connObj
cuObj = _cuObj
sqlsdObj = _sqlsdObj
wuObj = _wuObj
