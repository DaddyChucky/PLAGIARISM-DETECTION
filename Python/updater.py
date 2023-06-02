__title__       = 'updater.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> NORMALIZE PLSCs AND UPDATE INDIVIDUAL WEIGHT <--
###

from loadcsts import *
from json import load, dump

with open(FILE_OUT, "r") as F_IN:
    JSON_OUT_R = load(F_IN)


###
#   --> PART 1: NORMALIZE ONLY WEIGHT (NOT THE ORIGINAL RATIO) <--
###

for FILE in JSON_OUT_R:
    MIN_PLSC = 2
    for PLSC in FILE[JSONIZER_PLSCS]:
        if PLSC[0] < MIN_PLSC:
            MIN_PLSC = PLSC[0]
    for IDX, PLSC in enumerate(FILE[JSONIZER_PLSCS]):
        PLSC[0] -= MIN_PLSC
        JSON_OUT_R[IDX][JSONIZER_PLSCS][0] = PLSC


###
#   --> PART 2: SEEK MAX AND UPDATE WEIGHT AND PARENT <--
###

for IDX, FILE in enumerate(JSON_OUT_R):
    MAX_PLSC = (-1, "") # Weight, parent
    for PLSC in FILE[JSONIZER_PLSCS]:
        if PLSC[0] > MAX_PLSC[0]:
            MAX_PLSC = (PLSC[0], PLSC[2])
    JSON_OUT_R[IDX][JSONIZER_PLAGIARISM_WEIGHT]  = MAX_PLSC[0]
    JSON_OUT_R[IDX][JSONIZER_PARENT]             = MAX_PLSC[1]

with open(FILE_OUT, "w") as F_OUT:
    dump(JSON_OUT_R, F_OUT, indent=4, separators=(',', ': '))
