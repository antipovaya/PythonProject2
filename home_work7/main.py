from file_pack import task01 as hw

if __name__ == '__main__':
    print("Переименование txt файлов в каталоге files")
    files_cnt = hw.group_rename_files("my_file", ".txt", path="./files")
    print(f"Переименовано: {files_cnt}")

