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
            ORIGIN_CURRENT_LETTER   = ORIGIN[X - 1] if (X - 1) < len(ORIGIN) else ORIGIN[-1]
            EXTERNAL_CURRENT_LETTER = EXTERNAL[Y - 1] if (Y - 1) < len(EXTERNAL) else EXTERNAL[-1]
            
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
    PLSC_FINAL_WEIGHT = PLSC_WEIGHT[ARRAY_LENGTH[0] - 1, ARRAY_LENGTH[1] - 1]


    ###
    #   --> START BACKTRACKING <--
    ###

    PLSC = ""
    X, Y = ARRAY_LENGTH[0] - 1, ARRAY_LENGTH[1] - 1

    while PLSC_WEIGHT[X][Y] != 0 and PLSC_DIR[X][Y] != 0:
        if PLSC_DIR[X][Y] == DIAG_DIR:
            PLSC += ORIGIN[X - 1]
            X -= 1
            Y -= 1
        elif PLSC_DIR[X][Y] == TOP_DIR:
            X -= 1
        else:
            Y -= 1

    return round(PLSC_FINAL_WEIGHT / min(len(ORIGIN), len(EXTERNAL)), 5), "" + str(PLSC_FINAL_WEIGHT) + "/" + str(min(len(ORIGIN), len(EXTERNAL))), PLSC[::-1], 
