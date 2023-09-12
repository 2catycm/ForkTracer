import difflib
from git_operations import *

def calculate_similarity(repo1_path, repo2_path, version1=None, version2 = None):
    """
    计算两个 Git 仓库具体版本之间的文件内容相似度。
    """
    if not is_git_repository(repo1_path) or not is_git_repository(repo2_path):
        raise ValueError("输入路径不是有效的 Git 仓库")

    # 切换仓库到指定版本
    if version1 is not None:
        checkout_repository_to_version(repo1_path, version1)
    if version2 is not None:
        checkout_repository_to_version(repo2_path, version2)

    # 获取两个仓库的文件列表
    files1 = get_repository_files(repo1_path)
    files2 = get_repository_files(repo2_path)

    # 计算文件内容的相似度（以文件为单位）
    file_similarity_scores = {}
    for file1 in files1:
        if file1 in files2:
            similarity = calculate_file_similarity(os.path.join(repo1_path, file1), os.path.join(repo2_path, file1))
            file_similarity_scores[file1] = similarity

    return file_similarity_scores

 # 使用 difflib.SequenceMatcher 计算编辑距离




def calculate_file_similarity(file1_path, file2_path):
    """
    计算两个文件之间的相似度。
    """
    # 使用 difflib 库进行文件内容比较
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        text1 = file1.read()
        text2 = file2.read()

    # 使用 difflib.SequenceMatcher 计算相似度
    similarity = difflib.SequenceMatcher(None, text1, text2).ratio()

    return similarity

# 测试 calculate_similarity 函数
if __name__ == "__main__":
    repo1_path = "../bloomz.cpp"
    version1 = None
    repo2_path = "../FasterTransformer"
    version2 = None

    similarity_scores = calculate_similarity(repo1_path, repo2_path, version1, version2)
    print("文件内容相似度：")
    for file, similarity in similarity_scores.items():
        print(f"{file}: {similarity}")