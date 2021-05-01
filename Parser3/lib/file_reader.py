import os

def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()
        return data
    else:
        print("Input-файл не найден")





