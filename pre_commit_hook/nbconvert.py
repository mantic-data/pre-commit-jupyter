from __future__ import print_function

import argparse
import os
import sys
import subprocess

from isort import isort


def imports_incorrect(filename, show_diff=False):
    return isort.SortImports(filename, check=True, show_diff=show_diff).incorrectly_sorted


def main(argv=None):
    # subprocess.run([f'echo {sys.argv[0]} >> files.txt'], shell=True)
    # subprocess.run([f'echo {sys.argv[1]} >> files.txt'], shell=True)

    # parser = argparse.ArgumentParser()
    # parser.add_argument('filenames', nargs='*', help='Filenames to run')
    # parser.add_argument('--silent-overwrite', action='store_true', dest='silent', default=False)
    # parser.add_argument('--check-only', action='store_true', dest='check_only', default=False)
    # parser.add_argument('--diff', action='store_true', dest='show_diff', default=False)
    # args = parser.parse_args(sys.argv)
    # print(sys.argv)

    return_value = 0
    filename = sys.argv[1]
    #subprocess.run([f'echo {os.getcwd()} >> files.txt'], shell=True)
    #subprocess.run([f'echo {filename} >> files.txt'], shell=True)
    dir_py = os.path.dirname(filename) + '/py_scripts/'
    #dir_py = 'py_scripts/'
    #subprocess.run([f'echo {dir_py} >> files.txt'], shell=True)
    subprocess.run([f'mkdir {dir_py}'], shell=True)
    subprocess.run([f'git add {dir_py}'], shell=True)
    fpy = dir_py + os.path.splitext(os.path.basename(filename))[0]+'_notebook.py'
    subprocess.run([f'jupyter nbconvert --to script {filename} --stdout > {fpy}'], shell=True)
    subprocess.run([f'git add {fpy}'], shell=True)

    dir_html = os.path.dirname(filename) + '/notebooks_html/'
    subprocess.run([f'mkdir {dir_html}'], shell=True)
    subprocess.run([f'git add {dir_html}'], shell=True)
    fhtml = dir_html + os.path.splitext(os.path.basename(filename))[0]+'_notebook.html'
    subprocess.run([f'jupyter nbconvert --to html {filename} --stdout > {fhtml}'], shell=True)
    subprocess.run([f'git add {fhtml}'], shell=True)

    # for filename in args.filenames:
    #     subprocess.run([f'echo {os.getcwd()} >> files.txt'], shell=True)
    #     subprocess.run([f'echo {filename} >> files.txt'], shell=True)
    #     #dir_py = os.path.dirname(filename) + '/py_scripts/'
    #     dir_py = 'py_scripts/'
    #     subprocess.run([f'echo {dir_py} >> files.txt'], shell=True)
    #     subprocess.run([f'mkdir {dir_py}'], shell=True)
    #     subprocess.run([f'git add {dir_py}'], shell=True)
    #     fpy = dir_py + os.path.splitext(os.path.basename(filename))[0]+'_notebook.py'
    #     subprocess.run([f'jupyter nbconvert --to script {filename} --stdout > {fpy}'], shell=True)
    #     subprocess.run([f'git add {fpy}'], shell=True)




    #     if imports_incorrect(filename, show_diff=args.show_diff):
    #         if args.check_only:
    #             return_value = 1
    #         elif args.silent:
    #             isort.SortImports(filename)
    #         else:
    #             return_value = 1
    #             isort.SortImports(filename)
    #             print('FIXED: {0}'.format(os.path.abspath(filename)))
    return return_value

if __name__ == '__main__':
    exit(main())
