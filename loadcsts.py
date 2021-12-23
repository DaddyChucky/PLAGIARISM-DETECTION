__title__       = 'loadcsts.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'

###
#   --> GET CONSTANTS <--
###

from json import load
from os import getcwd
from os.path import join, exists, isdir

CONSTANTS_FILE_PATH  = 'constants.JSON'

try:
    with open(CONSTANTS_FILE_PATH) as CONSTANTS_FILE:
        CONSTANTS = load(CONSTANTS_FILE)

except FileNotFoundError as e:
    exit("FATAL: Could not find specified file", e)

try:
    FOLDER_NAME_OUT     = CONSTANTS["FOLDERS"]["OUT"]
    FOLDER_NAME_EXOS    = CONSTANTS["FOLDERS"]["EXOS"]
    
    FILE_NAME_OUT       = CONSTANTS["FILES"]["OUT"]
    
    DUMP_IGNORE         = CONSTANTS["FILES"]["DUMP_IGNORE"]

except KeyError as e:
    exit("FATAL: Could not find specified file", e)

FOLDER_PATH_OUT     = join(getcwd(), FOLDER_NAME_OUT)
FOLDER_PATH_EXOS    = join(getcwd(), FOLDER_NAME_EXOS)

FILE_OUT = join(FOLDER_PATH_OUT, FILE_NAME_OUT)

OUT_RICH_PRESENCE   = exists(FOLDER_PATH_OUT) and isdir(FOLDER_PATH_OUT)
EXOS_RICH_PRESENCE  = exists(FOLDER_PATH_EXOS) and isdir(FOLDER_PATH_EXOS)

JSONIZER_CURRENT_FILE   = "FILE"
JSONIZER_PARENT_FILE    = "PARENT"

JSONIZER_NAME               = "NAME"
JSONIZER_PLAGIARISM_WEIGHT  = "WEIGHT"
JSONIZER_CONTENT            = "CONTENT"
JSONIZER_SIZE               = "SIZE"
JSONIZER_LAST_MODIFICATION  = "LAST_MODIFICATION"
JSONIZER_PLSCS              = "PLSCS"

JSONIZER_PARENT_PLAGIARISM_WEIGHT   = "PARENT_WEIGHT"
JSONIZER_PARENT_NAME                = "PARENT_NAME"
JSONIZER_PARENT_SIZE                = "PARENT_SIZE"
JSONIZER_PARENT_LAST_MODIFICATION   = "PARENT_LAST_MODIFICATION"
JSONIZER_PARENT_PLSCS               = "PARENT_PLSCS"
