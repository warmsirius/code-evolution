def sync(reader, filesystem, src_root, dest_root):
    src_hashes = reader(src_root)
    dest_hashes = reader(dest_root)

    for sha, filename in src_hashes.items():
        if sha not in dest_hashes:
            srcpath = src_root / filename
            destpath = dest_root / filename
            filesystem.copy(destpath, srcpath)
        
        elif dest_hashes[sha] != filename:
            olddestpath = dest_root / filename
            newdestpath = dest_root / dest_hashes[sha]
            filesystem.move(olddestpath, newdestpath)

    for sha, filename in dest_hashes.items():
        if sha not in src_hashes:
            filesystem.delete(dest_root / filename)



