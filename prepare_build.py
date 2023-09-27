"""
Before we get here, the build environment has already been 
populated with the necessary conda and pip packages
and a conda environment is loaded
"""

import subprocess, os, sys, shutil
here = os.path.dirname(__file__)

# pip install teqp
# subprocess.check_call([sys.executable, '-m','pip','install teqp'], shell=True)

# or build from source ???
print('Finished prepare_build.py')

os.makedirs("externals/teqp/doc/source/_static", exist_ok=True)
os.makedirs("externals/teqp/doc-BORGED/source/_static", exist_ok=True)
shutil.copy2("externals/teqp/doc-BORGED/macros.tex", "externals/teqp/doc")

os.chdir('externals/teqp/doc-BORGED/source')

import sys
sys.path.append(os.path.abspath(os.curdir))

import sphinx_pre_run
sphinx_pre_run.run()

os.chdir(os.path.dirname(__file__))
shutil.move("externals/teqp/doc/source/_static/doxygen", "externals/teqp/doc-BORGED/source/_static/doxygen")