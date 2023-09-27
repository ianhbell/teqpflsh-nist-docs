"""
Before we get here, the build environment has already been 
populated with the necessary conda and pip packages
and a conda environment is loaded
"""

import subprocess, os, sys
here = os.path.dirname(__file__)

# pip install teqp
subprocess.check_call([sys.executable, '-m','pip','install teqp'], shell=True)

# or build from source ???
print('Finished prepare_build.py')