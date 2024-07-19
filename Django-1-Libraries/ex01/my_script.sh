#!/bin/bash

echo "Pip version is: " $(pip3 --version)
python3 -m venv local_lib
source local_lib/bin/activate

if [[ "$VIRTUAL_ENV" != "" ]]; then
    pip install --force-reinstall git+https://github.com/jaraco/path.git > path_install.log
fi

touch my_program.py
MY_PROGRAM_CONTENT='''#!/usr/bin/env python3


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
'''

echo $MY_PROGRAM_CONTENT > my_program.py
