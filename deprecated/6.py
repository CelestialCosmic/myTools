import os

def list_directories_with_depth(path, output_file, max_depth):
    with open(output_file, 'w', encoding='utf-8') as f:
        def traverse(current_path, current_depth):
            if current_depth > max_depth:
                return
            # 获取当前层级的子文件夹
            for dir_name in os.listdir(current_path):
                try:
                    full_path = os.path.join(current_path, dir_name)
                    if os.path.isdir(full_path):
                        # 根据深度添加缩进展示层级关系
                        f.write('  ' * current_depth + dir_name + '\n')
                        # 递归进入下一级目录
                        traverse(full_path, current_depth + 1)
                except:continue

        # 从初始路径开始遍历
        traverse(path, 0)

# 使用方法：替换 'your_directory_path' 为起始目录路径
list_directories_with_depth('G:/', 'out2.txt', 4)
