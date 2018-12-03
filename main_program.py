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
    albums = [(line) for line in albums if artist and album_name not in line]
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
    display.print_program_menu(['Delete Album by Artist and Album', 'Albums by Genre', 'Genre Stats', 'Last Oldest Album', 'Oldest of Genre'])
    while True:
        try:
            option = input('Choose an option: ')
            if option == '0':
                delete_album_by_artist_and_album_name(albums, input("Artist's name: "), input("Album's name: "))
            if option == '1':
                display.print_albums_list(music_reports.get_albums_by_genre(albums, input('Genre: ')))
            if option == '2':
                print(music_reports.get_genre_stats(albums))
            if option == '3':
                print(music_reports.get_last_oldest(albums))
            if option == '4':
                print(music_reports.get_last_oldest_of_genre(albums, input('Genre: ')))
            else:
                raise KeyError
        except KeyError:
            continue
                

if __name__ == '__main__':
    main()