__title__       = 'jsonizer.py'
__version__     = '1.0.0'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'

###
#   --> GET CONSTANTS <--
###

from genericpath import getsize
import json

CONSTANTS_FILE_PATH  = 'constants.JSON'

try:
    with open(CONSTANTS_FILE_PATH) as CONSTANTS_FILE:
        CONSTANTS = json.load(CONSTANTS_FILE)

except FileNotFoundError as e:
    exit("FATAL: Could not find specified file", e)

try:
    FOLDER_NAME_OUT     = CONSTANTS["FOLDERS"]["OUT"]
    FOLDER_NAME_EXOS    = CONSTANTS["FOLDERS"]["EXOS"]
    
    FILE_NAME_OUT       = CONSTANTS["FILES"]["OUT"]

except KeyError as e:
    exit("FATAL: Could not find specified file", e)


###
#   --> CHECK FOLDER RICH PRESENCE <--
###

from os import path, getcwd, mkdir, listdir
from os.path import getsize as gs, isfile

FOLDER_PATH_OUT = path.join(getcwd(), FOLDER_NAME_OUT)
FOLDER_PATH_EXOS = path.join(getcwd(), FOLDER_NAME_EXOS)

OUT_RICH_PRESENCE   =   path.exists(FOLDER_PATH_OUT) and path.isdir(FOLDER_PATH_OUT)
EXOS_RICH_PRESENCE  =   path.exists(FOLDER_PATH_EXOS) and path.isdir(FOLDER_PATH_EXOS)

print(FOLDER_PATH_EXOS, FOLDER_PATH_OUT)

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

else:
    if not sum(gs(f) for f in listdir(FOLDER_PATH_EXOS) if isfile(f)):
        exit(f"WARNING: No exercices found in {FOLDER_PATH_EXOS}")


###
#   --> JSONIZE EVERY FILE IN EXOS <--
###

JSONIZER_CURRENT_FILE   = "FILE"
JSONIZER_PARENT_FILE    = "PARENT"

JSONIZER_PLAGIARISM_WEIGHT  = "WEIGHT"
JSONIZER_NAME               = "NAME"
JSONIZER_SIZE               = "SIZE"
JSONIZER_LAST_MODIFICATION  = "LAST_MODIFICATION"
JSONIZER_PLSCS              = "PLSCS"

JSONIZER_PARENT_PLAGIARISM_WEIGHT   = "PARENT_WEIGHT"
JSONIZER_PARENT_NAME                = "PARENT_NAME"
JSONIZER_PARENT_SIZE                = "PARENT_SIZE"
JSONIZER_PARENT_LAST_MODIFICATION   = "PARENT_LAST_MODIFICATION"
JSONIZER_PARENT_PLSCS               = "PARENT_PLSCS"

JSONIZER = {
    JSONIZER_CURRENT_FILE: {
        JSONIZER_PLAGIARISM_WEIGHT: 0,
        JSONIZER_NAME: "",
        JSONIZER_SIZE: 0,
        JSONIZER_LAST_MODIFICATION: "",
        JSONIZER_PLSCS: [[]],
    },
    JSONIZER_PARENT_FILE: {
        JSONIZER_PARENT_PLAGIARISM_WEIGHT: 0,
        JSONIZER_PARENT_NAME: "",
        JSONIZER_PARENT_SIZE: 0,
        JSONIZER_PARENT_LAST_MODIFICATION: "",
        JSONIZER_PARENT_PLSCS: [[]],
    }
}