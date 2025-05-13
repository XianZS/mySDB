import os
import sys

sys.path.append(os.getcwd())
# Format:from .file import class as _class
from src.config.sqlStorageDir import SqlSD as _SqlSD

# Instantiate class objects that enable = _Enable()
sqlSD = _SqlSD()
