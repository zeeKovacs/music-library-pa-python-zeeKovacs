def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """


def get_albums_by_year(albums, year):
    """
    Get albums by year

    :param list albums: albums' data
    :param int year: year to filter by

    :returns: all albums released in the given year
    :rtype: list
    """


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """


def get_year_stats(albums):
    """
    Get albums' statistics showing how many albums were released by year
    Example: { 1972: 22, 1988: 13, 2000: 10, 2010: 33 }

    :param list albums: albums' data
    :returns: year stats
    :rtype: dict
    """


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """


def get_shortest_album(albums):
    """
    Get album with smallest value in length field.
    If there are more than one such album return the last (by original lists' order)

    :param list albums: albums' data
    :returns: shortest album
    :rtype: list
    """


def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """


def get_first_youngest(albums):
    """
    Get first album with latest release year.
    If there is more than one album with latest release year return the first
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: first youngest album
    :rtype: list
    """


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """


def get_first_youngest_of_genre(albums, genre):
    """
    Get first album with latest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: first youngest album in genre
    :rtype: list
    """


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """


def get_average_albums_length(albums):
    """
    Get avg of lengths of all albums in minutes, rounded to 2 decimal places
    Example: (3:51 + 5:20) / 2 = 4.59
             (231 + 320) seconds / 2 = 275.5 seconds

    :param list albums: albums' data
    :returns: average albums' length in minutes
    :rtype: float
    """
