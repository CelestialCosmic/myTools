import os
import shutil
import stat

def remove_readonly(func, path, exc_info):
    """
    回调函数，处理只读属性问题。
    当删除操作因只读属性失败时，
    通过 os.chmod 将目标文件/文件夹设置为可写，
    然后再次执行删除操作。
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clear():
    # 1. 从"blacklist.txt"中读取待删除的文件/文件夹名称（每行一个）
    try:
        with open("E:/code/tools/extract/rubbishList", "r", encoding="utf8") as f:
            blacklist = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"读取 blacklist.txt 文件失败: {e}")
        return

    # 2. 用户输入需要处理的文件夹
    base_dir = input("输入需要处理的文件夹路径: ").strip()
    if not os.path.isdir(base_dir):
        print("输入的路径无效，请检查后重试。")
        return

    # 3. 遍历文件夹下所有的文件与子文件夹
    # 借助os.walk, topdown=False保证文件在子目录被删除之前先处理子项
    for root, dirs, files in os.walk(base_dir, topdown=False):
        # 处理文件（注意只比较名称是否在黑名单中）
        for name in files:
            if name in blacklist:
                file_path = os.path.join(root, name)
                try:
                    # 取消只读属性
                    os.chmod(file_path, stat.S_IWRITE)
                    os.remove(file_path)
                    print(f"已删除文件: {file_path}")
                except Exception as e:
                    print(f"删除文件 {file_path} 时出错: {e}")
        
        # 处理目录
        for name in dirs:
            if name in blacklist:
                dir_path = os.path.join(root, name)
                try:
                    # 使用shutil.rmtree删除目录，遇到只读时由回调进行处理
                    shutil.rmtree(dir_path, onexc=remove_readonly)
                    print(f"已删除文件夹: {dir_path}")
                except Exception as e:
                    print(f"删除文件夹 {dir_path} 时出错: {e}")

    print("处理完成。")

if __name__ == "__main__":
    clear()
