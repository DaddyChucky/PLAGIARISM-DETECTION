__title__       = 'revealcheats.py'
__author__      = 'DE LAFONTAINE, Charles'
__copyright__   = 'DE LAFONTAINE, Charles; 2021-2022'

from loadcsts import *
from json import load, dump

class bcolors: # FROM https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

###
#   --> FIND BEST CHEAT POTENTIAL <--
###


with open(FILE_OUT, "r") as F_IN:
    JSON_OUT_R = load(F_IN)

UPPER_BOUND = 0.75
LOWER_BOUND = 0.25

for IDX, FILE in enumerate(JSON_OUT_R):
    print(f"\nSummary for file #{IDX + 1} ({FILE[JSONIZER_NAME]}):")
    if FILE[JSONIZER_PLAGIARISM_WEIGHT] >= UPPER_BOUND:
        print(bcolors.BOLD + bcolors.FAIL + f"Found {round(FILE[JSONIZER_PLAGIARISM_WEIGHT] * 100, 2)}% similitude with {FILE[JSONIZER_PARENT]}" + bcolors.ENDC)
    elif FILE[JSONIZER_PLAGIARISM_WEIGHT] <= LOWER_BOUND:
        print(bcolors.OKGREEN + f"Found {round(FILE[JSONIZER_PLAGIARISM_WEIGHT] * 100, 2)}% similitude with {FILE[JSONIZER_PARENT]}" + bcolors.ENDC)
    else:
        print(bcolors.BOLD + bcolors.WARNING + f"Found {round(FILE[JSONIZER_PLAGIARISM_WEIGHT] * 100, 2)}% similitude with {FILE[JSONIZER_PARENT]}" + bcolors.ENDC)