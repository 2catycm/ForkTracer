from git_operations import *
from simularity import *
def find_fork_points(target_repo_path, potential_origin_repo_path):
    """
    执行核心分析功能，找到目标仓库可能的起源。
    """
    if not is_git_repository(target_repo_path) or not is_git_repository(potential_origin_repo_path):
        raise ValueError("输入路径不是有效的 Git 仓库")

    # 在这里编写分析逻辑
    # 包括历史版本的比较和相似度计算