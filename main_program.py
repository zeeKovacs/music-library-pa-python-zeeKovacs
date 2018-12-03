import music_reports
import display
import file_handling

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """
    for line in albums:
        if artist and album_name in line:
            albums.remove(line)
    file_handling.export_data(albums, filename='albums_data.txt', mode='w')
    pass



def main():
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """
    albums = file_handling.import_data(filename='albums_data.txt')
    display.print_program_menu(['Delete Album by Artist and Album', 'Albums by Genre', 'Not implemented yet.', 'Not implemented yet.'])
    while True:
        try:
            option = input('Choose an option: ')
            if option == '0':
                delete_album_by_artist_and_album_name(albums, input("Artist's name: "), input("Album's name: "))
            if option == '1':
                display.print_albums_list(music_reports.get_albums_by_genre(albums, input('Genre: ')))
            if option == '2':
                pass
            if option == '3':
                pass
            else:
                raise KeyError
        except KeyError:
            continue
                

if __name__ == '__main__':
    main()