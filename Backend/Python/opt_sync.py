import hashlib
import shutil
import os
from pathlib import Path
from typing import Dict, Generator, Tuple

BLOCKSIZE = 65536


FileName = str
Sha1Hash = str
PathHashes = Dict[Sha1Hash, FileName]
Action = Tuple[str, Path, Path] | Tuple[str, Path]


def sync(source: str, dest: str):
    # 命令式脚本第一步: 收集输入
    source_hashes = read_paths_and_hashes(source)
    dest_hashes = read_paths_and_hashes(dest)

    # 命令式脚本第二步: 调用行为
    actions = determine_actions(source_hashes, dest_hashes, source, dest)
    # 命令式脚本第三步: 执行行为、输出结果
    for action, *paths in actions:
        if action == 'COPY':
            src_path, dest_path = paths
            print(f"复制文件: 从 {src_path} 到 {dest_path}")
            shutil.copy(src_path, dest_path)
        elif action == 'MOVE':
            old_path, new_path = paths
            print(f"重命名文件: 从 {old_path} 到 {new_path}")
            shutil.move(old_path, new_path)
        elif action == 'DELETE':
            path, = paths
            print(f"删除文件: {path}")
            os.remove(path)

def hash_file(filepath: Path) -> str:
    """计算文件的SHA1哈希值"""
    hasher = hashlib.sha1()
    with filepath.open('rb') as f:
        while True:
            buf = f.read(BLOCKSIZE)
            if not buf:
                break
            hasher.update(buf)
    return hasher.hexdigest()


def read_paths_and_hashes(root: str) -> PathHashes:
    """读取目录下所有文件的hash值"""
    hashed = {}
    for folder, _, files in os.walk(root):
        for fn in files:
            hashed[hash_file(Path(folder) / fn)] = fn
    return hashed


def determine_actions(
        src_hashes: PathHashes, dst_hashes: PathHashes, 
        src_root: str, dst_root: str
    ) -> Generator[Action, None, None]:
    for sha, filename in src_hashes.items():
        # 如果目标目录没有该文件，复制文件
        if sha not in dst_hashes:
            sourcepath = Path(src_root) / filename
            destpath = Path(dst_root) / filename
            yield ('COPY', sourcepath, destpath)
        # 如果目标目录有该文件但文件名不同，重命名文件
        elif dst_hashes[sha] != filename:
            olddespath = Path(dst_root) / dst_hashes[sha]
            newdespath = Path(dst_root) / filename
            yield ('MOVE', olddespath, newdespath)
    
    for sha, filename in dst_hashes.items():
        # 如果目标目录有该文件但源目录没有，删除文件
        if sha not in src_hashes:
            destpath = Path(dst_root) / filename
            yield ('DELETE', destpath)
