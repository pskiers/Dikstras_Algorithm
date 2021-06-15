def read_form_file(file_name):
    table = []
    with open(file_name) as fh:
        content = fh.readlines()
        for line in content:
            row = [int(numb) for numb in str(line) if numb != '\n']
            table.append(row)
    return table
