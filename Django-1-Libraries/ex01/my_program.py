#!/usr/bin/env python3
from path import Path

new_folder = Path('new_folder_from_path')
new_folder.makedirs_p()
file = open('new_folder_from_path/new_file', 'w')
file.write("This is the file content")
file.close()
file = open('new_folder_from_path/new_file', 'r')
print(file.read())
