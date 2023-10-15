import os
from pathlib import Path

PATH_TO_ROOT = '../'
PATH_TO_RESOURCES = PATH_TO_ROOT + 'resources/'
PATH_TO_MID = PATH_TO_ROOT + 'output/midi/'
PATH_TO_MP3 = PATH_TO_ROOT + 'output/mp3/'


def find_root_folder(folder, cwd, count):
    if count > 100:
        return None
    return os.path.abspath(os.path.basename(folder)) if folder in os.listdir(cwd) else find_root_folder(folder, Path(cwd).parent, count+1)
