#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明：
1. 本程序要求系统环境中已安装 7-Zip 命令行工具（命令为“7z”）。
2. 密码列表存放在同目录下的 password.txt 中，每行一个密码（无需空行）。
3. 程序实现了智能判断文件是否为压缩包，即使扩展名被伪装也会尝试解压。
4. 针对 rar 和 zip 的分卷压缩包，程序依据文件名规则（例如：rar 分卷中非 part1 的直接跳过，zip 分卷只处理 .zip 文件）只对第一卷解压，并将该组所有文件在解压成功后整体移动到 done 文件夹。
5. 针对 tar.gz/tar.zst 等，先在临时目录中完全解压，然后进一步提取 tar 包内容到 extracted 文件夹。
"""
import clear_ai
import os
import re
import subprocess
import shutil
import sys
import tempfile

def read_passwords(password_file='E:/code/tools/extract/list/passwdList'):
    """
    从密码文件读取每个可能的密码，返回密码列表
    """
    try:
        with open(password_file, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]
        return passwords
    except Exception as e:
        print(f"读取密码文件失败: {e}")
        sys.exit(1)

def get_archive_group(file_path):
    """
    针对可能存在的分卷压缩包，利用文件名规则获取同组成员
    例如对于 rar：如果文件名为 aaa.part1.rar，则同目录下所有匹配 aaa.part\d+\.rar 或 aaa\.rar 均认为属于此组；
         对于 zip：.zip 文件认为是第一卷，后续 .z01/.z02 等则归为一组。
    返回一个排序后的同组文件列表（绝对路径）。
    """
    dir_path = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    group = [file_path]

    # 针对 rar 分卷处理
    if re.search(r'\.rar$', filename, re.IGNORECASE):
        m = re.match(r"(.+?)(?:\.part\d+)?\.rar$", filename, re.IGNORECASE)
        if m:
            base = m.group(1)
            # 遍历当前目录下所有文件
            for f in os.listdir(dir_path):
                if re.match(rf"{re.escape(base)}(?:\.part\d+)?\.rar$", f, re.IGNORECASE):
                    full_path = os.path.join(dir_path, f)
                    if full_path not in group:
                        group.append(full_path)
        return sorted(group)

    # 针对 zip 分卷处理：通常第一卷为 .zip，后续为 .z01, .z02 等
    elif filename.lower().endswith('.zip'):
        base = filename[:-4]
        for f in os.listdir(dir_path):
            if f.startswith(base) and (f.lower().endswith('.zip') or re.search(r'\.z\d{2}$', f.lower())):
                full_path = os.path.join(dir_path, f)
                if full_path not in group:
                    group.append(full_path)
        return sorted(group)

    # 其他情况当作独立压缩包
    return group

def is_archive(file_path, password=None):
    """
    利用 7z l 命令判断给定文件是否为一个能够被 7z 识别的压缩包。
    若 password 非空，则作为密码参数传入。
    """
    cmd = ["7z", "l", file_path]
    # 只有当 password 非空时才添加 -p 参数
    if password:
        cmd.insert(2, f"-p{password}")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def get_valid_password(file_path, passwords):
    """
    对于一个可能需要密码的压缩包，首先尝试不加密码；若不成功，再依次尝试密码列表，直到成功为止。
    返回空字符串表示不需要密码，若均不成功则返回 None。
    """
    if is_archive(file_path, password=""):
        return ""
    for pwd in passwords:
        if is_archive(file_path, password=pwd):
            return pwd
    return None

def extract_archive(archive_file, output_dir, password, special=False):
    """
    利用 7z 命令解压 archive_file 到 output_dir，支持传入密码。
    当 special 为 True 时，针对 tar.gz、tar.zst（及 tgz）的情况，
    先解压到临时目录，再检查是否有 tar 文件需要进一步解压。
    返回 True 表示解压成功，否则返回 False。
    """
    if special:
        # 创建临时目录用于第一次解压
        temp_dir = tempfile.mkdtemp()
        try:
            cmd = ["7z", "x", archive_file, f"-o{temp_dir}"]
            if password:
                cmd.insert(2, f"-p{password}")
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode != 0:
                return False

            # 检测临时目录内是否存在 .tar 文件
            tar_found = False
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    if file.lower().endswith(".tar"):
                        tar_filepath = os.path.join(root, file)
                        # 直接调用 7z 对 tar 进行解压
                        cmd2 = ["7z", "x", tar_filepath, f"-o{output_dir}"]
                        result2 = subprocess.run(cmd2, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        if result2.returncode != 0:
                            return False
                        tar_found = True

            # 如果没有 tar 文件，则将临时目录中的所有内容移动（或复制）到 output_dir
            if not tar_found:
                for item in os.listdir(temp_dir):
                    s = os.path.join(temp_dir, item)
                    d = os.path.join(output_dir, item)
                    # 如果目标已经存在，可考虑覆盖或跳过，可根据需要调整此处逻辑
                    shutil.move(s, d)
            return True
        finally:
            shutil.rmtree(temp_dir)
    else:
        cmd = ["7z", "x", archive_file, f"-o{output_dir}"]
        if password:
            cmd.insert(2, f"-p{password}")
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0

def main(folder):
    passwords = read_passwords()
    # folder = input("请输入需要解压的文件夹路径: ").strip()
    if not os.path.exists(folder) or not os.path.isdir(folder):
        print("文件夹不存在。")
        sys.exit(1)

    # 在目标文件夹下创建 “extracted” 和 “done” 子文件夹
    extracted_dir = os.path.join(folder, "extracted")
    done_dir = os.path.join(folder, "done")
    os.makedirs(extracted_dir, exist_ok=True)
    os.makedirs(done_dir, exist_ok=True)

    # 遍历目标文件夹内部所有文件（递归），排除 extracted 和 done 文件夹下的文件
    candidate_files = []
    for root, dirs, files in os.walk(folder):
        # 排除 “extracted” 和 “done” 文件夹
        if os.path.abspath(root).startswith(os.path.abspath(extracted_dir)) or \
           os.path.abspath(root).startswith(os.path.abspath(done_dir)):
            continue
        for file in files:
            candidate_files.append(os.path.join(root, file))

    # 记录已处理（或移动）的文件，避免重复处理分卷中多次操作
    processed = set()

    for file_path in candidate_files:
        if file_path in processed:
            continue
        # 调用 get_valid_password 判断该文件是否为压缩包或其是否需要密码
        valid_pwd = get_valid_password(file_path, passwords)
        if valid_pwd is None:
            # 非压缩包或无法识别，直接跳过
            continue

        # 针对分卷压缩包做归类
        group = get_archive_group(file_path)
        # 对于 rar 分卷，若文件名中包含 “part” 但不是 part1.rar，则说明不是第一卷，跳过处理
        filename_lower = os.path.basename(file_path).lower()
        if filename_lower.endswith('.rar'):
            if "part" in filename_lower and not re.search(r'\.part1\.rar$', filename_lower):
                processed.add(file_path)
                continue
        # 对于 zip 分卷，只对扩展名为 .zip 的文件处理
        if any(filename_lower.endswith(ext) for ext in [".z01", ".z02", ".z03"]):
            processed.add(file_path)
            continue

        # 如果是 tar.gz、tgz 或 tar.zst，则标记为需要 special 处理
        special = False
        if filename_lower.endswith(('.tar.gz', '.tgz', '.tar.zst')):
            special = True

        print(f"正在解压: {file_path}")
        success = extract_archive(file_path, extracted_dir, valid_pwd, special)
        if success:
            print(f"解压成功: {file_path}")
            # 如果解压成功，则将整个组内所有文件都移动到 done 文件夹
            for arch in group:
                try:
                    target = os.path.join(done_dir, os.path.basename(arch))
                    # 如果目标文件已存在，可以选择覆盖或者更名
                    shutil.move(arch, target)
                    processed.add(arch)
                except Exception as e:
                    print(f"移动文件失败: {arch}, 错误: {e}")
        else:
            print(f"解压失败: {file_path}")
            processed.add(file_path)

if __name__ == "__main__":
    folder = input("请输入需要解压的文件夹路径\n").strip()
    main(folder)
    clear_ai.clear(folder)