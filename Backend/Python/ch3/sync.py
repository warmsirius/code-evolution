import hashlib
import os
import shutil
from pathlib import Path


BLOCKSIZE = 65536

def hash_file(filepath):
    """hash文件"""
    hasher = hashlib.sha1()
    with filepath.open('rb') as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BLOCKSIZE)
    return hasher.hexdigest()


def sync(source, dest):
    # 源目录的所有文件hash
    source_hashses = {}
    for folder, _, files in os.walk(source):
        for fn in files:
            # hash_file(Path(folder) / fn) Path(folder) / fn 是 Python 中 pathlib 模块的路径操作方法
            # 创建了一个完整的文件路径，相当于: os.path.join(folder, fn)
            source_hashses[hash_file(Path(folder) / fn)] = fn
    
    seen = set() # 目标目录中已经有的文件

    for folder, _, files in os.walk(dest):
        for fn in files:
            dest_path = Path(folder) / fn
            dest_hash = hash_file(dest_path)
            seen.add(dest_hash)

            # 如果源不存在，目标存在，删除文件
            if dest_hash not in source_hashses:
                print(f"删除文件: {dest_path}")
                dest_path.unlink()
            # 如果源存在，目标存在，但文件名不同，重命名文件
            elif dest_path in source_hashses and fn != source_hashses[dest_hash]:
                shutil.move(dest_path, Path(folder) / source_hashses[dest_hash])

    # 复制源目录中目标目录不存在的文件
    for src_hash, fn in source_hashses.items():
        if src_hash not in seen:
            shutil.copy(Path(source) / fn, Path(dest) / fn)


