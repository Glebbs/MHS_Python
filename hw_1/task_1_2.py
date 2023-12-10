import sys

def tail(file=None, num_lines=10):
    if file:
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()
        num_lines = 17

    if len(lines) > num_lines:
        lines = lines[-num_lines:]

    for line in lines:
        print(line.rstrip())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print(f'=> {sys.argv[1]} <=')
        tail(sys.argv[1])
        for file in sys.argv[2:]:
            print(f'\n=> {file} <=')
            tail(file)
    else:
        tail()