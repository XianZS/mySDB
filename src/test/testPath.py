from pathlib import Path


path_1 = r"./"
p_obj_1 = Path(path_1)
print(p_obj_1.is_absolute())

path_2 = "D:/"
p_obj_2 = Path(path_2)
print(p_obj_2.is_absolute())
