#!/bin/bash

echo "Pip version is: " $(pip3 --version)
python3 -m venv local_lib
source local_lib/bin/activate

if [[ "$VIRTUAL_ENV" != "" ]]; then
    pip install --force-reinstall git+https://github.com/jaraco/path.git > path_install.log
fi

touch my_program.py

cat << EOF > my_program.py
#!/usr/bin/env python3
from path import Path

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