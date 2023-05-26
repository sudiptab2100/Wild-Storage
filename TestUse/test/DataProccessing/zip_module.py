import zipfile
import os
import sys

class ZipModule:
    def __init__(self, ztype=1):
        self.ztype = ztype

    def zip(self, fname, target_dir, op_dir):          
        zipobj = zipfile.ZipFile(op_dir + fname + '.zip', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(target_dir) + 1
        for base, dirs, files in os.walk(target_dir):
            for file in files:
                fn = os.path.join(base, file)
                zipobj.write(fn, fn[rootlen: ])
    
    def unzip(self, fname, target_dir, op_dir):
        with zipfile.ZipFile(target_dir, 'r') as zip:
            zip.extractall(op_dir + fname + '/')

