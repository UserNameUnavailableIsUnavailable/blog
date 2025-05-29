import json
import yaml
import os
import re
import shutil
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()

project_dir = os.path.dirname(__file__)
output_dir = os.path.join(project_dir, "blog")
ignore_dirs = ["blog", ".git", ".quarto", "assets"] # 忽略的文件夹名称
traverse_dirs: list = [] # 遍历的文件夹，内容为“文件夹名-最近一次生成边栏文件时间”键值对

with open(os.path.join(project_dir, "project.json")) as json_file:
    traverse_dirs = json.load(json_file)

# 解析 RMarkdown 文件
def ResolveRMarkdown(file_path: str) -> str:
    title = ""
    metadata = {}
    with open(file_path, "r", encoding="utf8") as file:
        content = file.read()
        match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            try:
                metadata = yaml.safe_load(yaml_content)
            except: # 非法 YAML 格式
                return title
            if isinstance(metadata, dict) and "title" in metadata:
                if (isinstance(metadata["title"], str)):
                    title = metadata["title"]
    return title

def MakeSymbolicLink(path: str, target: str, force: bool = False):
    print(f"{path} -> {target}")
    exists = os.path.lexists(path)
    if (exists):
        if (force):
            os.remove(path)
        else:
            return
    os.symlink(target, path)

def GenerateTableOfContents(directory: str, parent_sidebar: object = {})-> None:
    # 计算 directory 的相对于项目根目录的相对路径
    relative_directory_path = os.path.relpath(directory, project_dir)
    relative_directory_path = "/" + relative_directory_path + "/" if (relative_directory_path != ".") else "/"
    relative_directory_path = relative_directory_path.replace("\\", "/")

    contents = {} # 本级目录的边栏内容
    back = [{"type": "document", "title": "⤴︎", "href": f"{relative_directory_path}../index.html"}] # 返回上一级
    index = [] # 子目录的索引文件

    sidebar_lock_path = os.path.join(directory, "sidebar.lock.json")
    sidebar_lock = False
    if (os.path.exists(sidebar_lock_path)):
        with open(sidebar_lock_path, "r", encoding="utf8") as file:
            contents = json.loads(file.read())
            sidebar_lock = True
    
    if (not sidebar_lock): # 没有 sidebar.lock.json，进行目录内容解析
        index_path = os.path.join(directory, "index.qmd") # 检查目录下是否存在 index.qmd 文件
        if (os.path.isfile(index_path)):
            title = ResolveRMarkdown(index_path) # 解析标题
            index.append({"type": "document", "title": title, "href": f"{relative_directory_path}index.html", "active": True}) # 添加索引
        else:
            return

        contents = {
            "type": "section", # sidebar 的类型
            "title": title, # sidebar 的标题
            "href": f"{relative_directory_path}index.html", # sidebar 的路径
            "children": [] # sidebar 的子项
        }

        rel_subdir_paths = [] # 子目录

        # 遍历目录下的所有 qmd 文件，生成 sidebar
        for rel_item_path in os.listdir(directory): # 遍历目录下的所有文件和子目录
            abs_item_path = os.path.join(directory, rel_item_path) # 计算绝对路径
            if (rel_item_path in ignore_dirs): # 如果在忽略列表中，跳过
                continue
            elif (rel_item_path == "index.qmd"): # index.qmd 已经单独处理
                continue
            elif os.path.isdir(abs_item_path): # 目录
                rel_subdir_paths.append(rel_item_path) # 子目录压栈，等常规文件处理完毕后再单独处理
            elif os.path.isfile(abs_item_path) and rel_item_path.endswith(".qmd"): # qmd 文件
                title = ResolveRMarkdown(abs_item_path) # 解析标题
                if title:
                    item_name = os.path.basename(rel_item_path) # 获取文件名
                    item_name = re.sub(r"\.qmd$", ".html", item_name)
                    contents["children"].append({"type": "document", "title": title, "href": f"{relative_directory_path}{item_name}"})

        # 针对目录做进行递归处理
        for rel_subdir_path in rel_subdir_paths:
            GenerateTableOfContents(os.path.join(directory, rel_subdir_path), contents) # 递归调用处理子目录

        if (not "children" in parent_sidebar):
            parent_sidebar["children"] = []
    # 两种情况：
    # 1. 将 sidebar 直接添加到父级目录的 sidebar 中
    # 2. 将 sidebar 单独保存在 sidebar.json 中，作为独立的边栏导航区
    # 不论哪种情况，都会在父级边栏添加子目录的索引（需要保证 index.qmd 存在）
    seperate = True
    metadata_path = os.path.join(directory, "_metadata.yml") # 检查目录下是否存在 _metadata.yml 文件
    if (os.path.isfile(metadata_path)):
        with open(metadata_path, "r", encoding="utf8") as file:
            metadata = yaml.safe_load(file)
            if isinstance(metadata, dict) and "SeparateSidebar" in metadata:
                if isinstance(metadata["SeparateSidebar"], bool): # 确保是布尔值
                    seperate = metadata["SeparateSidebar"] # 确定是否单独建立边栏导航区

    sidebar_link_target = os.path.normpath("../sidebar.json") # Windows 原生支持正反斜线作为路径分隔符，因此这里用不用 normpath 都无所谓
    if not seperate:
        parent_sidebar["children"].append(contents) # 将索引添加到父级边栏
        sidebar_path = os.path.join(directory, "sidebar.json")
        MakeSymbolicLink(sidebar_path, sidebar_link_target, True)
    else: # 分离，建立新的边栏导航区
        contents["children"] = back + index + contents["children"]
        parent_sidebar["children"].append({"type": "document", "title": contents["title"], "href": contents["href"]}) # 将索引添加到父级边栏
        if len(contents["children"]) > 2:
            contents["type"] = "root"
            json_string = json.dumps(contents, indent = 4, ensure_ascii = False)
            path = os.path.join(directory, "sidebar.json")
            if (os.path.exists(path)):
                os.remove(path)
            with open(path, "w", encoding = "utf8") as file:
                file.write(json_string)
        else:
            sidebar_path = os.path.join(directory, "sidebar.json")
            MakeSymbolicLink(sidebar_path, sidebar_link_target, True)
    
if __name__ == "__main__":
    if (not os.path.exists(output_dir)):
        os.makedirs(output_dir)
    for item in traverse_dirs:
        path = os.path.join(project_dir, item)
        GenerateTableOfContents(path)
        # _tp = os.path.getmtime(path) # 最近一次修改时间
        # if (_tp < tp):
        #     continue
        for root, dirs, filenames in os.walk(os.path.join(project_dir, item), topdown = False, onerror = None, followlinks = False):
            for filename in filenames:
                if (filename == "sidebar.json"):
                    rel_path = os.path.relpath(root, project_dir)
                    output_path = os.path.join(output_dir, rel_path)
                    print(output_path)
                    if (not os.path.exists(output_path)):
                        os.makedirs(output_path)
                    target = os.path.join(root, filename)
                    path = os.path.join(output_path, filename)
                    if (os.path.islink(target)):
                        MakeSymbolicLink(path, os.readlink(target), True)
                    else:
                        shutil.copyfile(target, path)
        # traverse_dirs[item] = os.path.getmtime(path) # 修改为当前时间
    json_string = json.dumps(traverse_dirs, indent=4, ensure_ascii=False)
    with open(os.path.join(project_dir, "project.json"), "w", encoding="utf8") as file:
        file.write(json_string)