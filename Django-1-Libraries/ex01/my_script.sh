#!/bin/bash

echo -e "Pip version is:\n"$(pip3 --version)"\n"

if [ ! -d "path" ]; then
    git clone https://github.com/jaraco/path.git
else
    echo -e "Directory 'path' already exists!\n"
fi
if [ -d "local_lib" ]; then
    echo -e "Overwriting and re-installing the library\n" 
    rm -rf local_lib
fi
mkdir local_lib
pip install path --target=local_lib > path_install.log
touch my_program.py

cat << EOF > my_program.py
#!/usr/bin/env python3
from local_lib.path import Path

new_folder = Path('new_folder')
new_folder.makedirs_p()
file = open('new_folder/new_file', 'w')
file.write("This is the file content")
file.close()
file = open('new_folder/new_file', 'r')
print(file.read())
EOF

python3 my_program.py

#rm -rf new_folder
#rm -rf local_lib