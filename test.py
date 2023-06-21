# folder size recursively calculator
import os
import sys
import time
import shutil


def show_folder_size(folder_path):
    """

    Purpose: print the size of the folders in the folder_path
        """
    for root, dirs, files in os.walk(folder_path):
        print(root, "consumes")
        print(sum([os.path.getsize(os.path.join(root, name))
              for name in files]))
        print("bytes in", len(files), "non-directory files")
        if '.git' in dirs:
            dirs.remove('.git')  # don't visit git directories'
        if '.vscode' in dirs:
            dirs.remove('.vscode')
        if '.ipynb_checkpoints' in dirs:
            dirs.remove('.ipynb_checkpoints')
        if 'venv' in dirs:
            dirs.remove('venv')
        print(dirs, "comsumes")
        print(sum([os.path.getsize(os.path.join(root, name))
              for name in dirs]))
        print("bytes in", len(dirs), "directory files")

# test show_folder_size() with  "d:\\code"
# main()


show_folder_size("d:\\code")
