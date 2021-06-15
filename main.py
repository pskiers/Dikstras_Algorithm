import argparse
from dirstra import dikstra
from read_map import read_form_file


def main(file_name):
    graph = read_form_file(file_name)
    print(dikstra(graph))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='enter file name')
    args = parser.parse_args()
    main(args.name)
