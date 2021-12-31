# This project is continued on [GitLab](https://gitlab.com/DaddyChucky/PLAGIARISM-DETECTION)!
# COPYRIGHT
## © 2021-2022; DE LAFONTAINE, Charles.

- Reproduction for commercial use is stricly prohibited and would, therefore, be quite contradictory to this project's sole purpose. 
- Free for personal usage. 
- Need new functionalities? [Contact me!](https://www.linkedin.com/in/charles-de-lafontaine-2506191b2/)

# PROJECT GOAL
Plagiarism detection between students' copies.

# USAGE

- First start? Launch *jsonizer.py* to help you make **EXOS** and **OUT** directories. 
- Then, simply put a **ZIP** or a Project folder inside the **EXOS** directory newly created.
- Define the constants for the files and extra folders to ignore while dezipping in *constants.JSON*.
- For a quick start, run *oneliner.py*.
- For an advanced start, run *dezipper.py* followed by *jsonizer.py*. After this *jsonizer.py* launch, you will see *plscOut.JSON* in your **OUT** directory. You may open it to see all the 'compiled' files and, perhaps, reajust your constants in *constants.JSON*. After that, launch *comparer.py* which calculates the PLSCs of all files listed in your *plscOut.JSON*. Once that step is finished, run *updater.py* which will normalize to the smallest weight all the PLSCs found. The last step is to run *revealcheats.py* which reveals all the potential cheaters depending on the PLSCs.

## FILE EXTENT DESCRIPTION

### **EXOS**/*plscOut.JSON*

File containing the weight, parent, name, content, size, last modification, and a list of PLSCs for every file 'compiled' based on your *constants.JSON* settings.

### *constants.JSON*

File containing the name of the folders created, as well as the files to be ignored when *jsonizer.py* is ran.

### *dezipper.py*

Unzips all the zip files contained in **EXOS** to mere folders.

### *plsc.py*

Calculates all the PLSCs of the files defined in **EXOS**/*plscOut.JSON*, and not present in ignores of *constants.JSON*.

### *jsonizer.py*

Creates **EXOS** and **OUT** folders (if not already created), then runs *plsc.py*

### *loadcsts.py*

Loads constants of *constants.JSON*. Imported in practically every project file but useless to run individually.

### *oneliner.py*

Runs the whole program in simply one execution. Risky, because you have to know its execution well.

### *comparer.py*

Once PLSCs are done calculating, this file is ran to adjust the final weight and parent of every file.

### *updater.py*

Normalizes every weight of every file by substracting the minimum weight.

### *revealcheats.py*

Reads *plscOut.JSON* and reveals potential cheaters.

# Version log / TODO

- 1.0, working great on Windows. Although, eats too much time for 100+ copies (hours). Need to refine that work.
- Better, refined *updater.py*
