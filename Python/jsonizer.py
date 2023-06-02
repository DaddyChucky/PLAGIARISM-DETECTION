__title__       = 'jsonizer.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> CHECK FOLDER RICH PRESENCE <--
###

from loadcsts import *
from os import mkdir, listdir
from genericpath import getsize
from os.path import isfile, join, getmtime

if not OUT_RICH_PRESENCE and not EXOS_RICH_PRESENCE:
    mkdir(FOLDER_PATH_OUT)
    mkdir(FOLDER_PATH_EXOS)
    exit("WARNING NO-CONTENT: Folders OUT and EXOS were created.")

elif not OUT_RICH_PRESENCE:
    mkdir(FOLDER_PATH_OUT)
    exit("WARNING PARTIAL-NO-CONTENT: Folder OUT was created.")

elif not EXOS_RICH_PRESENCE:
    mkdir(FOLDER_PATH_EXOS)
    exit("WARNING PARTIAL-NO-CONTENT: Folder EXOS was created.")


###
#   --> JSONIZE EVERY FILE IN EXOS <--
###

JSONIZER = {
    JSONIZER_PLAGIARISM_WEIGHT: 0.,
    JSONIZER_PARENT: "",
    JSONIZER_NAME: "",
    JSONIZER_CONTENT: [],
    JSONIZER_SIZE: 0,
    JSONIZER_LAST_MODIFICATION: "",
    JSONIZER_PLSCS: [],
}

from json import dump
from time import ctime
from copy import deepcopy

DUMP_LIST = []

i = 0

PATHS = listdir(FOLDER_PATH_EXOS)
while True: # DFS
    try:
        CURRENT_PATH = join(FOLDER_PATH_EXOS, PATHS.pop(0))
        for DIR in listdir(CURRENT_PATH):
            DIR_PATH = join(CURRENT_PATH, DIR)

            VALID = True
            for IGNORE in FOLDER_IGNORE + FILE_IGNORE:
                VALID = True
                if DIR.lower()[:len(IGNORE)] == IGNORE.lower() or DIR.lower()[-len(IGNORE):] == IGNORE.lower():
                    VALID = False
                    break
            
            if not VALID: 
                continue
            
            if isdir(DIR_PATH):
                PATHS.append(DIR_PATH)
            else:
                i += 1
                F_PATH = DIR_PATH
                if isfile(F_PATH):
                    DUMPER = JSONIZER
                    DUMPER[JSONIZER_NAME]               = F_PATH
                    DUMPER[JSONIZER_SIZE]               = getsize(F_PATH)
                    DUMPER[JSONIZER_LAST_MODIFICATION]  = ctime(getmtime(F_PATH))
                    with open(F_PATH, mode='r', encoding="utf8") as F_CONTENT:
                        try:
                            content = F_CONTENT.read()
                        except UnicodeDecodeError:
                            content = ""
                        for ignores in DUMP_IGNORE:
                            content = content.replace(ignores, '').replace(ignores.upper(), '').replace(ignores.capitalize(), '').replace(ignores.title(), '').lower()
                        DUMPER[JSONIZER_CONTENT] = content
                    DUMP_LIST.append(deepcopy(DUMPER))
       
    except IndexError:
        break



with open(FILE_OUT, "w") as F_OUT:
    dump(DUMP_LIST, F_OUT, indent=4, separators=(',', ': '))

TOTAL_FILES = i + 1
match TOTAL_FILES:
    case 1:
        print(f"Successfully compiled {TOTAL_FILES} file in {FOLDER_PATH_OUT + FILE_NAME_OUT}")
    case _:
        print(f"Successfully compiled {TOTAL_FILES} files in {FOLDER_PATH_OUT + FILE_NAME_OUT}")
