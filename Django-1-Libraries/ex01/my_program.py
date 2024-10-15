#!/usr/bin/env python3
from local_lib.path import Path

new_folder = Path('new_folder')
new_folder.makedirs_p()
file = open('new_folder/new_file', 'w')
file.write("This is the file content")
file.close()
file = open('new_folder/new_file', 'r')
print(file.read())
