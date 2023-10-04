import hashlib
import glob
import sys
import os

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
            
    print(hash_md5.hexdigest())
    return hash_md5.hexdigest()
    

pathOut = sys.argv[2]
if os.path.exists(pathOut):
  os.remove(pathOut)

pathIn = sys.argv[1]
if pathIn[len(pathIn)-1] == '/':
   path1 = pathIn + "*"
else:
   path1 = pathIn + "/*"

fileList = glob.glob(path1)
print(fileList)

f = open(pathOut, "x")

for x in fileList:
   f.write(md5(x)+"\n")