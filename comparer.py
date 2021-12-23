__title__       = 'comparer.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> READ FILES AND START COMPARISON <--
###

from loadcsts import *
from plsc import PLSC
from json import load, dump

with open(FILE_OUT, "r") as F_OUT:
    JSON_OUT_R = load(F_OUT)

for I_IDX, I_FILE in enumerate(JSON_OUT_R):
    ITERATED_FILE           = I_FILE[JSONIZER_CURRENT_FILE]
    ITERATED_FILE_WEIGHT    = ITERATED_FILE[JSONIZER_PLAGIARISM_WEIGHT]
    ITERATED_FILE_CONTENT   = ITERATED_FILE[JSONIZER_CONTENT]
    ITERATED_FILE_NAME      = ITERATED_FILE[JSONIZER_NAME]
    ITERATED_FILE_PLSCS     = ITERATED_FILE[JSONIZER_PLSCS]

    # *** There will be duplicate calculations, although the check costs more than the doubled calculations
    # i.e. file b checks file c, file c checks file b, although the check of other's file name in current's PLSCs requires iteration over all PLSCs
    # Sometimes, it's okay to be lazy if it also saves you programming time :) I love you too. - CDL, 2021.
    for C_IDX, C_FILE in enumerate(JSON_OUT_R):
        if I_IDX != C_IDX: # Do not compare file with itself
            COMPARED_FILE           = C_FILE[JSONIZER_CURRENT_FILE]
            COMPARED_FILE_NAME      = COMPARED_FILE[JSONIZER_NAME]
            COMPARED_FILE_CONTENT   = COMPARED_FILE[JSONIZER_CONTENT]
            PLSC_RES                = PLSC(ITERATED_FILE_CONTENT, COMPARED_FILE_CONTENT)
            if COMPARED_FILE_NAME == ITERATED_FILE_NAME or [PLSC_RES[1], PLSC_RES[2]] in ITERATED_FILE_PLSCS: continue # Do not compare file with itself deep check continue
            # Update file PLSCS
            JSON_OUT_R[I_IDX][JSONIZER_CURRENT_FILE][JSONIZER_PLSCS].append(list(PLSC_RES))
            # Update file weight if applicable
            if PLSC_RES[0] > JSON_OUT_R[I_IDX][JSONIZER_CURRENT_FILE][JSONIZER_PLAGIARISM_WEIGHT]:
                JSON_OUT_R[I_IDX][JSONIZER_CURRENT_FILE][JSONIZER_PLAGIARISM_WEIGHT] = PLSC_RES[0]
                # Also update parent name for future help
                JSON_OUT_R[I_IDX][JSONIZER_CURRENT_FILE][JSONIZER_PARENT] = JSON_OUT_R[C_IDX][JSONIZER_CURRENT_FILE][JSONIZER_NAME]

with open(FILE_OUT, "w") as F_OUT:
    dump(JSON_OUT_R, F_OUT, indent=4, separators=(',', ': '))
