import argparse
from gendiff.gendiff_engine import generate_diff


NAME = 'gendiff'
DESCRIPTION = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(
                                    prog=NAME,
                                    description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                       help='set format of output',
                       default='stylish')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
