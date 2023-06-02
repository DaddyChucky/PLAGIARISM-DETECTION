__title__       = 'jsonizer.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> CHECK FOLDER RICH PRESENCE <--
###

from loadcsts import *
from os import mkdir, rmdir, walk, makedirs, remove
from os.path import join, exists
from zipfile import Path, ZipFile

def unzip(path: Path, total_count: int = 0): # https://stackoverflow.com/questions/36285502/how-to-extract-zip-file-recursively
    for root, _, files in walk(path):
        for file in files:
            file_name = join(root, file)
            if (not file_name.endswith('.zip') and not isdir(file)):
                total_count += 1
            else:
                currentdir = file_name[:-4]
                try:
                    if not exists(currentdir):
                        makedirs(currentdir)
                    with ZipFile(file_name) as zipObj:
                        zipObj.extractall(currentdir)
                    remove(file_name)
                except Exception:
                    continue
                total_count = unzip(currentdir, total_count)
    return total_count

if not EXOS_RICH_PRESENCE:
    mkdir(FOLDER_PATH_EXOS)
    quit(f"WARNING NO-CONTENT: Created folder {FOLDER_PATH_EXOS}")

unzip(FOLDER_PATH_EXOS)
print(f"Successfully unzipped all files in {FOLDER_PATH_EXOS}")
