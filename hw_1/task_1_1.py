import sys


def nl(file=None):
    if file:
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines, start=1):
        print(f'{i}\t{line.rstrip()}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl()
