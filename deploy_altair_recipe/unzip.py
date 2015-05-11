import zipfile
import os
import os.path
import shutil
import sys

from utils import get_diskspace


USAGE_MESSAGE = 'usage: %s filepath [target_dir]' % __file__


def get_target():
    if   len(sys.argv)==2:
        filepath = sys.argv[1]
        target_dir, _ = filepath.rsplit('.', 1)
    elif len(sys.argv)==3:
        filepath, target_dir = sys.argv[1:]
    else:
        exit(USAGE_MESSAGE)

    if os.path.exists(target_dir):
        exit('"%s" already exists\n' % (target_dir))

    filesize = os.path.getsize(filepath)
    diskspace = get_diskspace(os.path.split(filepath)[0])
    if not filesize*1.5 < diskspace:
        exit('File size:  %s\n'
             'Disk space: %s\n'
             'Disk space is not 1.5 times of file size\n' % (filesize, diskspace))

    return filepath, target_dir


def unzip(filepath, target_dir):
    with zipfile.ZipFile(filepath) as z:
        try:
            print('extract %s to %s ...\n' % (filepath, target_dir))
            os.makedirs(target_dir)
            for fn in z.namelist():
                print('extract %s ...' % (fn))
                z.extract(fn, path=target_dir)
            #z.extractall(path=target_dir)
            print('\nextract file successfully\n')
        except KeyboardInterrupt:
            shutil.rmtree(target_dir)
            exit('\n')


if __name__=='__main__':
    unzip(*get_target())
