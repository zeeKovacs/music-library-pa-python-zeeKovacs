import file_handling

def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    return [lines for lines in albums if genre == lines[3]]


def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """
    stats = {}
    for lines in albums:
        if lines[3] not in stats:
            stats.update({lines[3]:0})    
        stats[lines[3]] += 1
    return stats

def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
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
    min = 3000
    for lines in albums:
        if int(lines[2]) < min:
            min = int(lines[2])
    oldest = [lines for lines in albums if str(min) in lines]
    return oldest[-1]


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    filtered = [(lines) for lines in albums if genre in lines]
    min = 3000
    for lines in filtered:
        if int(lines[2]) < min:
            min = int(lines[2])
    filtered_year = [line for line in filtered if str(min) in line]
    return filtered_year[0]


def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
