import os
import subprocess

def is_directory(path):
    return os.path.isdir(path)

def is_git_repository(path):
    """
    检查给定路径是否是一个 Git 仓库。
    """
    # 在指定路径下运行 git rev-parse 命令来判断是否为仓库
    try:
        subprocess.check_call(['git', 'rev-parse'], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
    
def get_repository_history(repo_path):
    """
    获取一个 Git 仓库的历史版本名称或哈希值列表。
    """
    if not is_git_repository(repo_path):
        raise ValueError("输入路径不是有效的 Git 仓库")

    # 在 Git 中，每个提交都有一个唯一的哈希值
    # 我们可以使用 "git log" 命令来获取提交历史的信息
    try:
        result = subprocess.check_output(['git', 'log', '--format=%H'], cwd=repo_path, stderr=subprocess.PIPE)
        # 使用换行符分割获取的哈希值列表
        history = result.decode('utf-8').split('\n')[:-1]  # 去除最后一个空行
        return history
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"无法获取仓库历史：{e}")

def checkout_repository_to_version(repo_path, version):
    """
    将一个 Git 仓库切换到指定版本。
    """
    if not is_git_repository(repo_path):
        raise ValueError("输入路径不是有效的 Git 仓库")

    # 在这里编写切换版本的逻辑
    
    
def get_repository_files(repo_path):
    """
    获取一个 Git 仓库的文件列表（排除.git目录）。
    """
    if not is_git_repository(repo_path):
        raise ValueError("输入路径不是有效的 Git 仓库")

    # 使用 git ls-files 命令获取仓库中的文件列表
    try:
        result = subprocess.check_output(['git', 'ls-files'], cwd=repo_path, stderr=subprocess.PIPE)
        files = result.decode('utf-8').split('\n')[:-1]  # 去除最后一个空行
        return [file for file in files if not file.startswith('.git/')]
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"无法获取仓库文件列表：{e}")
    
# 测试 is_git_repository 函数
if __name__ == "__main__":
    # repo_path = "../../../FasterTransformer"
    repo_path = "../FasterTransformer"
    if is_git_repository(repo_path):
        print(f"{repo_path} 是一个 Git 仓库")
    else:
        print(f"{repo_path} 不是一个 Git 仓库")

    # 测试 get_repository_history 函数
    history = get_repository_history(repo_path)
    print("仓库历史版本：")
    print(len(history))
    for commit_hash in history:
        print(commit_hash)