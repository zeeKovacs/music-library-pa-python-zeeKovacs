def import_data(filename='albums_data.txt'):
    with open(filename, 'r') as f:
        return [line.strip().split(',') for line in f]


def export_data(albums, filename='albums_data.txt', mode='a'):
    with open(filename, mode) as f:
        if mode == 'w' or mode =='a':
            for lines in albums:
                f.write(','.join(lines))
                f.write('\n')
        else:
            raise ValueError('Wrong write mode')
