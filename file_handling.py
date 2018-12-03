def import_data(filename='albums_data.txt'):
    with open(filename, 'r') as f:
        return [line.strip().split(',') for line in f]


def export_data(albums, filename='albums_data.txt', mode='a'):
    if mode != 'w' or mode != 'a':
       raise ValueError('Wrong write mode')
    with open(filename, mode) as f:
        [f.write(','.join(lines)) for lines in albums]
