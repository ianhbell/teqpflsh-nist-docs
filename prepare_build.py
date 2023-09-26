"""
Before we get here, the build environment has already been 
populated with the necessary conda and pip packages
and a conda environment is loaded
"""

import subprocess, os
here = os.path.dirname(__file__)

# Checkout teqp
subprocess.check_output("git clone https://github.com/usnistgov/teqp", shell=True, cwd=here)

# And build???
