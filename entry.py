import argparse
import os


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--silent-overwrite', action='store_true', dest='silent', default=False)
    parser.add_argument('--check-only', action='store_true', dest='check_only', default=False)
    parser.add_argument('--diff', action='store_true', dest='show_diff', default=False)
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:
        print('FIXED: {0}'.format(os.path.abspath(filename)))
    return return_value


if __name__ == '__main__':
    exit(main())
