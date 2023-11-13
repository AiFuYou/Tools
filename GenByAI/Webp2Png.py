# pip install Pillow命令安装了Pillow库

import os
from PIL import Image

def convert_webp_to_png(input_dir, output_dir):
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".webp"):
            # 构建输入文件的完整路径
            input_path = os.path.join(input_dir, filename)
            
            # 构建输出文件的完整路径
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.png")

            try:
                # 打开webp文件并保存为png文件
                im = Image.open(input_path).convert("RGBA")
                im.save(output_path, "PNG")
                print(f"转换成功：{output_path}")
            except Exception as e:
                print(f"转换失败：{input_path}，错误信息：{e}")

# 指定输入目录和输出目录
input_dir = "源目录"
output_dir = "目标目录"

# 调用函数进行转换
convert_webp_to_png(input_dir, output_dir)