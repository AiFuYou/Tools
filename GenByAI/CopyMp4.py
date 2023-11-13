import os
import shutil

def filter_and_copy(source_dir, destination_dir, folder_keyword, filename_keyword):
    # 获取指定目录下的所有文件夹
    folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f)) and folder_keyword in f]

    # 遍历每个文件夹
    for folder in folders:
        folder_path = os.path.join(source_dir, folder)
        
        # 获取文件夹中包含指定关键字的mp4文件
        mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4') and filename_keyword in f]
        
        # # 将每个mp4文件拷贝到目标文件夹
        for mp4_file in mp4_files:
            src_file = os.path.join(folder_path, mp4_file)
            dst_file = os.path.join(destination_dir, mp4_file)
            shutil.move(src_file, dst_file)

    print("移动完成！")

# 指定源文件夹和目标文件夹
source_directory = '源目录'
destination_directory = '目标目录'

# 指定文件夹关键字和文件名关键字
folder_keyword = '关键字1'
filename_keyword = '关键字2'

# 调用函数进行过滤和拷贝
filter_and_copy(source_directory, destination_directory, folder_keyword, filename_keyword)