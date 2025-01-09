# teqpflsh-docs-ntd2d

A repo for holding docs for teqpflsh. The generated docs live in the ``nist-pages`` branch and are auto-generated via a github action. The code of teqpflsh is integrated via a git submodule

To update the docs:

1. Make sure the most updated wheels of ``teqpflsh`` have already been pushed to PYPI. These binary wheels are installed into the conda environment used to build the docs and must be new enough to support all function calls in the docs.
2. In a shell in ``externals/teqpflsh``, do a ``git pull origin main``.
3. Commit the updated submodule to this repo, and push
4. The github action should fire (check https://github.com/ianhbell/teqpflsh-nist-docs/actions ).