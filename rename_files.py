# renames all files in the given directory by removing all numbers in file names
# used to solve a mixed picture puzzle with a secret message

import os
import string

current_dir = os.getcwd() # current directory
foldername = 'secret_message' # folder of pictures/files to be renamed
path = current_dir + '\\'+ foldername # create path to folder of files to rename

file_list = os.listdir(path) # create list of filenames

def rename_files(file_list):
    for item in file_list:
        new_name = item.translate(None,'0123456789')
        os.chdir(path)
        os.rename(item, new_name)

rename_files(file_list)
