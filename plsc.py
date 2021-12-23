__title__       = 'plsc.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'


###
#   --> PLSC <--
###

from numpy import int8, ndarray, chararray, str0

def PLSC(ORIGIN: str, EXTERNAL: str) -> tuple():
    ARRAY_LENGTH    = (len(ORIGIN) + 1, len(EXTERNAL) + 1)
    DIAG_DIR        = 11
    LEFT_DIR        = 10
    TOP_DIR         = 1
    PLSC_WEIGHT     = ndarray((ARRAY_LENGTH[0], ARRAY_LENGTH[1]), dtype=int8)
    PLSC_DIR        = ndarray((ARRAY_LENGTH[0], ARRAY_LENGTH[1]), dtype=int8)

    PLSC_WEIGHT.fill(0)
    PLSC_DIR.fill(0)

    for X in range(1, ARRAY_LENGTH[0]):
        for Y in range(1, ARRAY_LENGTH[1]):
            ORIGIN_CURRENT_LETTER   = ORIGIN[Y - 1] if (Y - 1) < len(ORIGIN) else ORIGIN[-1]
            EXTERNAL_CURRENT_LETTER = EXTERNAL[X - 1] if (X - 1) < len(EXTERNAL) else EXTERNAL[-1]

            DIAG    = PLSC_WEIGHT[X - 1][Y - 1]
            TOP     = PLSC_WEIGHT[X - 1][Y]
            LEFT    = PLSC_WEIGHT[X][Y - 1]

            if ORIGIN_CURRENT_LETTER == EXTERNAL_CURRENT_LETTER:
                PLSC_WEIGHT[X][Y]   = DIAG + 1
                PLSC_DIR[X][Y]      = DIAG_DIR

            else:
                if TOP >= LEFT:
                    PLSC_WEIGHT[X][Y]   = TOP
                    PLSC_DIR[X][Y]      = TOP_DIR
                else:
                    PLSC_WEIGHT[X][Y]   = LEFT
                    PLSC_DIR[X][Y]      = LEFT_DIR

    # PLSC Array construction is finished. Let's iterate backwards to retrieve the PLSC.
    PLSC_FINAL_WEIGHT = PLSC_WEIGHT[ARRAY_LENGTH[0], ARRAY_LENGTH[1]]

    ###
    #   --> START BACKTRACKING <--
    ###

    PLSC = ""
    for x in range(ARRAY_LENGTH[0]):
        for y in range (ARRAY_LENGTH[1]):

PLSC("ABAT", "ABBASFSFA")

###
#   --> READ FILES AND START COMPARISON <--
###

# from loadcsts import *
# from json import load

# with open(FILE_OUT, "r") as F_OUT:
#     JSON_OUT_R = load(F_OUT)

# for I_FILE in JSON_OUT_R:
#     ITERATED_FILE           = I_FILE[JSONIZER_CURRENT_FILE]
#     ITERATED_FILE_CONTENT   = ITERATED_FILE[JSONIZER_CONTENT]
#     ITERATED_FILE_NAME      = ITERATED_FILE[JSONIZER_NAME]

#     for C_FILE in JSON_OUT_R:
#         COMPARED_FILE           = C_FILE[JSONIZER_CURRENT_FILE]
#         COMPARED_FILE_NAME      = COMPARED_FILE[JSONIZER_NAME]
        
#         if COMPARED_FILE_NAME != ITERATED_FILE_NAME: # Do not compare file with itself
#             COMPARED_FILE_CONTENT = COMPARED_FILE[JSONIZER_CONTENT]
#             NEW_PLSC_WEIGHT = PLSC(ITERATED_FILE_CONTENT, COMPARED_FILE_CONTENT)
