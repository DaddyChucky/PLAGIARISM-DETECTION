__title__       = 'comparer.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'

from time import time
START_TIME = time()
print("Job started!")

from loadcsts import *
from plsc import PLSC
from json import load, dump
from threading import Thread

###
#   --> READ FILES AND START COMPARISON <--
###

with open(FILE_OUT, "r") as F_OUT:
    JSON_OUT_R = load(F_OUT)

def calculate_plsc(I_IDX, ITERATED_FILE, ITERATED_FILE_WEIGHT, ITERATED_FILE_CONTENT, ITERATED_FILE_NAME, ITERATED_FILE_PLSCS, CUTOFF_LOW: int = -1, CUTOFF_HIGH: int = -1):
    # *** There will be duplicate calculations, although the check costs more than the doubled calculations
    # i.e. file b checks file c, file c checks file b, although the check of other's file name in current's PLSCs requires iteration over all PLSCs
    # Sometimes, it's okay to be lazy if it also saves you programming time :) I love you too. y- CDL, 2021.
    for C_IDX, C_FILE in enumerate(JSON_OUT_R):
        if I_IDX != C_IDX and C_IDX >= CUTOFF_LOW and C_IDX <= CUTOFF_HIGH: # Do not compare file with itself
            COMPARED_FILE_NAME      = C_FILE[JSONIZER_NAME]
            COMPARED_FILE_CONTENT   = C_FILE[JSONIZER_CONTENT]
            PLSC_RES                = PLSC(ITERATED_FILE_CONTENT, COMPARED_FILE_CONTENT, COMPARED_FILE_NAME)
            if COMPARED_FILE_NAME == ITERATED_FILE_NAME or [PLSC_RES[1], PLSC_RES[2]] in ITERATED_FILE_PLSCS: continue # Do not compare file with itself deep check continue
            # Update file PLSCs
            JSON_OUT_R[I_IDX][JSONIZER_PLSCS].append(list(PLSC_RES))

THREADS = []

CUTOFF_FACTOR = 5
CUTOFFS = [tuple([i * CUTOFF_FACTOR, (i + 1) * CUTOFF_FACTOR - 1]) for i in range(len(JSON_OUT_R) // CUTOFF_FACTOR + 1)]
CUTOFFS[-1] = (CUTOFFS[-1][0], len(JSON_OUT_R)) # In case size is not % CUTOFF_FACTOR (last job the longest just like Windows)
print(f"JOB CUTOFFS --> {CUTOFFS}")

for I_IDX, I_FILE in enumerate(JSON_OUT_R):
    ITERATED_FILE_WEIGHT    = I_FILE[JSONIZER_PLAGIARISM_WEIGHT]
    ITERATED_FILE_CONTENT   = I_FILE[JSONIZER_CONTENT]
    ITERATED_FILE_NAME      = I_FILE[JSONIZER_NAME]
    ITERATED_FILE_PLSCS     = I_FILE[JSONIZER_PLSCS]
    for SUBTHREAD in range(len(CUTOFFS)):
        THREADS.append(Thread(
            target = calculate_plsc, 
            name = I_IDX,
            args = (I_IDX, I_FILE, ITERATED_FILE_WEIGHT, ITERATED_FILE_CONTENT, ITERATED_FILE_NAME, ITERATED_FILE_PLSCS, CUTOFFS[SUBTHREAD][0], CUTOFFS[SUBTHREAD][1])
        ))

for I, THREAD in enumerate(THREADS):
    THREAD.start()
    THREAD.join()
    print("Computing...", round((I + 1) / (len(JSON_OUT_R) * len(CUTOFFS)) * 100, 2), "%")

with open(FILE_OUT, "w") as F_OUT:
    dump(JSON_OUT_R, F_OUT, indent=4, separators=(',', ': '))

FINAL_TIME = time() - START_TIME
MIN_TO_SEC = 60
MIN = FINAL_TIME // MIN_TO_SEC
SEC = round(FINAL_TIME - MIN * MIN_TO_SEC, 2)

print("Job finished in", MIN, "min", SEC, "s!")
