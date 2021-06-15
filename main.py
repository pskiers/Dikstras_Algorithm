from dirstra import dikstra
from read_map import read_form_file

if __name__ == "__main__":
    file_name = input('Enter name of file with the table: ')
    graph = read_form_file(file_name)
    print(dikstra(graph))