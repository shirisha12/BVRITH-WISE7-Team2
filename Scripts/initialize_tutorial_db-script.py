#!d:\pyramid\tutorial\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tutorial','console_scripts','initialize_tutorial_db'
__requires__ = 'tutorial'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tutorial', 'console_scripts', 'initialize_tutorial_db')()
    )
