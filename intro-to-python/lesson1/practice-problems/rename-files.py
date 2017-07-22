import os
import re

working_directory = r"/Users/lbuthman/PycharmProjects/udacity-nanodegree/intro-to-python/lesson1/example-files/prank"


def rename_files():
    file_list = os.listdir(working_directory)

    os.chdir(working_directory)
    for file_name in file_list:
        new_file_name = re.sub("\d+", "", file_name)
        print("Old file name: ", file_name)
        os.rename(file_name, new_file_name)
        print("New file name: ", new_file_name)

rename_files()
