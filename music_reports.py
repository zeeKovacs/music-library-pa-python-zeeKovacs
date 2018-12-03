import file_handling

def get_albums_by_genre(albums, genre):
    if any(genre in line for line in albums):
        return [lines for lines in albums if genre == lines[3]]
    raise ValueError('Wrong genre')


def get_genre_stats(albums):
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
    time = []
    for lines in albums:
        minutes = int(lines[4].split(':')[0]) * 60
        time.append(minutes + int(lines[4].split(':')[1]))
    max = 0
    for k in time:
        if k > max:
            max = k
    for l, maxtime in enumerate(time):
        if time[l] == max:
            return albums[l]
    


def get_last_oldest(albums):
    min = 3000
    for lines in albums:
        if int(lines[2]) < min:
            min = int(lines[2])
    oldest = [lines for lines in albums if str(min) in lines]
    return oldest[-1]


def get_last_oldest_of_genre(albums, genre):
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
    time = []
    for lines in albums:
        minutes = int(lines[4].split(':')[0]) * 60
        time.append(minutes + int(lines[4].split(':')[1]))
    return sum(time)/60