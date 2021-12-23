__title__       = 'plsc.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> READ FILES AND START COMPARISON <--
###

from loadcsts import *
from json import load

with open(FILE_OUT, "r") as F_OUT:
    JSON_OUT_R = load(F_OUT)

for I_FILE in JSON_OUT_R:
    ITERATED_FILE           = I_FILE[JSONIZER_CURRENT_FILE]
    ITERATED_FILE_CONTENT   = ITERATED_FILE[JSONIZER_CONTENT]
    ITERATED_FILE_NAME      = ITERATED_FILE[JSONIZER_NAME]

    for C_FILE in JSON_OUT_R:
        COMPARED_FILE           = C_FILE[JSONIZER_CURRENT_FILE]
        COMPARED_FILE_NAME      = COMPARED_FILE[JSONIZER_NAME]
        
        if COMPARED_FILE_NAME != ITERATED_FILE_NAME: # Do not compare file with itself
            COMPARED_FILE_CONTENT = COMPARED_FILE[JSONIZER_CONTENT]
            