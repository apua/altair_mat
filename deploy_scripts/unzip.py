import zipfile
import os.path
import os

filepath = 'ICsp-vmware-7.5.0-20150314.zip'

with zipfile.ZipFile(filepath) as f:
    #dirname, filename = os.path.split(filepath)
    dirname, filename = filepath.rsplit('.', 1)
    print(dirname, filename)
    if os.path.exists(dirname):
        raise OSError("{} exists".format(dirname))
    os.makedirs(dirname)
    f.extractall(path=dirname)
