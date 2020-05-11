from cx_Freeze import setup , Executable

setup(name = "my_exe", version = '0.1',description = 'stuff', executables = [Executable("image_processing.py")])