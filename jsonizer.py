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
    JSONIZER_CURRENT_FILE: {
        JSONIZER_NAME: "",
        JSONIZER_PLAGIARISM_WEIGHT: 0,
        JSONIZER_CONTENT: [],
        JSONIZER_SIZE: 0,
        JSONIZER_LAST_MODIFICATION: "",
        JSONIZER_PLSCS: [],
    },
    JSONIZER_PARENT_FILE: {
        JSONIZER_PARENT_PLAGIARISM_WEIGHT: 0.,
        JSONIZER_PARENT_NAME: "",
        JSONIZER_PARENT_SIZE: 0,
        JSONIZER_PARENT_LAST_MODIFICATION: "",
        JSONIZER_PARENT_PLSCS: [[]],
    }
}

from json import dump
from time import ctime
from copy import deepcopy

DUMP_LIST = []

i = 0
for i, f in enumerate(listdir(FOLDER_PATH_EXOS)):
    F_PATH = join(FOLDER_PATH_EXOS, f)
    if isfile(F_PATH):
        DUMPER = JSONIZER
        DUMPER[JSONIZER_CURRENT_FILE][JSONIZER_NAME] = f
        DUMPER[JSONIZER_CURRENT_FILE][JSONIZER_SIZE] = getsize(F_PATH)
        DUMPER[JSONIZER_CURRENT_FILE][JSONIZER_LAST_MODIFICATION] = ctime(getmtime(F_PATH))
        with open(F_PATH, mode='r') as F_CONTENT:
            content = F_CONTENT.read()
            for ignores in DUMP_IGNORE:
                content = content.replace(ignores, '').replace(ignores.upper(), '').replace(ignores.capitalize(), '').replace(ignores.title(), '')
            DUMPER[JSONIZER_CURRENT_FILE][JSONIZER_CONTENT] = content
        DUMP_LIST.append(deepcopy(DUMPER))

with open(FILE_OUT, "w") as F_OUT:
    dump(DUMP_LIST, F_OUT, indent=4, separators=(',', ': '))

TOTAL_FILES = i + 1
match TOTAL_FILES:
    case 1:
        print(f"Successfully compiled {TOTAL_FILES} file in {FOLDER_PATH_OUT + FILE_NAME_OUT}")
    case _:
        print(f"Successfully compiled {TOTAL_FILES} files in {FOLDER_PATH_OUT + FILE_NAME_OUT}")
