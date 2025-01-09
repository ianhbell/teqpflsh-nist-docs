"""
Before we get here, the build environment has already been 
populated with the necessary conda and pip packages
and a conda environment is loaded
"""

import subprocess, os, sys, shutil
here = os.path.dirname(__file__)
# print(os.environ)

# https://stackoverflow.com/a/70129189
# subprocess.check_call("pip uninstall -y teqp sphinxcontrib-doxylink", shell=True)
# # subprocess.check_call("conda remove -y `conda list|awk 'NR>3 {print $1}'|tr '\n' ' '`", shell=True)
# subprocess.check_call("conda install python=3.10", shell=True)
# print('Removing complete')
# subprocess.check_call('conda env update --name base --file environment.yml --solver libmamba', shell=True)
# print('Env updating complete')
# subprocess.check_call('conda list', shell=True)

# # Copy back from doc-BORGED into doc some files that need to be in specific places
# os.makedirs("externals/teqp/doc/source/_static", exist_ok=True)
# os.makedirs("externals/teqp/doc-BORGED/source/_static", exist_ok=True)
# shutil.copy2("externals/teqp/doc-BORGED/macros.tex", "externals/teqp/doc")

# And now run doxygen and execute jupyter notebooks
os.chdir('externals/teqpflsh/doc/source')
sys.path.append(os.path.abspath(os.curdir))
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'
import sphinx_pre_run
sphinx_pre_run.run()

# # And move the doxygen docs back where they are needed in the doc-BORGED tree
# os.chdir(os.path.dirname(__file__))
# shutil.move("externals/teqp/doc/source/_static/doxygen", "externals/teqp/doc-BORGED/source/_static/doxygen")

print('Finished prepare_build.py')