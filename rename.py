import os
import glob
import datetime

def rename_files_by_date(directory):
    if not os.path.exists(directory):
        print("目录不存在")
        return
    
    files = glob.glob(os.path.join(directory, '*'))
    files.sort(key=os.path.getmtime)  # 按修改日期排序
    
    for index, file_path in enumerate(files):
        _, extension = os.path.splitext(file_path)
        new_name = f"{index+1:04d}{extension}"  # 使用四位数的阿拉伯数字作为新文件名
        new_path = os.path.join(directory, new_name)
        os.rename(file_path, new_path)
        print(f"重命名 {file_path} 为 {new_path}")

if __name__ == "__main__":
    target_directory = input("请输入目标目录的路径: ")
    rename_files_by_date(target_directory)
