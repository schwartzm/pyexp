from os import chdir
import argparse
from pathlib import Path
from random import randint
import shutil

parser = argparse.ArgumentParser(
    description='Generate text files of various byte lengths.',
    epilog='WARNING: Past generated files are deleted in ./files dir.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--num', type=int, default=10, help='number of files to create')
parser.add_argument('--min', type=int, default=50, help='minimum file size (bytes)')
parser.add_argument('--max', type=int, default=1000, help='maximum file size (bytes)')
args = parser.parse_args()

def main():
    folder = Path.cwd() / 'files'
    if folder.is_dir():
        shutil.rmtree(folder)
    
    folder.mkdir()

    for f in range(1, args.num + 1):
        size = randint(args.min, args.max)
        path = Path(f'{folder}/{f}-{size}.txt')
        path.touch()
        path.write_text('x'*size)

if __name__ == "__main__":
    main()