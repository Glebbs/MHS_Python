import sys


def wc(file=None):
    if file:
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    byte_count = sum(len(line.encode('utf-8')) for line in lines)

    return line_count, word_count, byte_count


if __name__ == '__main__':
    if len(sys.argv) > 1:
        total_line_count = 0
        total_word_count = 0
        total_byte_count = 0
        for file in sys.argv[1:]:
            line_count, word_count, byte_count = wc(file)
            print(f'{line_count} {word_count} {byte_count} {file}')
            total_line_count += line_count
            total_word_count += word_count
            total_byte_count += byte_count
        if len(sys.argv) > 2:
            print(f'{total_line_count} {total_word_count} {total_byte_count} total')
    else:
        line_count, word_count, byte_count = wc()
        print(f'{line_count} {word_count} {byte_count}')
