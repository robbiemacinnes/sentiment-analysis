import tarfile

with tarfile.open("../data/external/aclImdb_v1.tar.gz", "r:gz") as tar:
    tar.extractall()
