# Only albums with this RYM score and higher get selected
min_score = 10


import itertools
import random


with open("data/rym.txt", 'r', encoding="utf-8") as infile, \
     open("data/output.txt", 'w', encoding="utf-8") as outfile, \
     open("data/filter.txt", 'r', encoding="utf-8") as filterfile:

    # Data preparation

    filters = filterfile.readlines()
    filters = [line.rstrip() for line in filters] # strip newlines for filtering

    lines = infile.readlines()
    lines = [line.rstrip() for line in lines]

    albums = []

    # Data filter
    new_lines = filter(lambda line: not any(filter in line for filter in filters), lines)

    # Data formatting

    for line in new_lines:
        line_elements = line.replace('"', '').split(',')

        rym_score = 0 if line_elements[7] == '' else int(line_elements[7])
        if rym_score < min_score:
            continue

        formatted_line = "{} {} {} {}  - {} ({})".format(line_elements[1],
                                                         line_elements[2],
                                                         line_elements[3],
                                                         line_elements[4],
                                                         line_elements[5],
                                                         line_elements[6])
        albums.append({
            'title': formatted_line,
            'score': 0
        })

    # gathers all unique album-album combos. Amount of combinations grows extremely quickly
    # but there's no better way to find, say, the top 10 albums.
    combinations = list(itertools.combinations(albums, 2))
    print('There are', len(combinations), 'combinations.')
    random.shuffle(combinations)

    for combination in combinations:
        print('')
        print('1. ', combination[0]['title'])
        print('2. ', combination[1]['title'])
        answer = input('Which album do you prefer? ')
        if answer == '1':
            albums[albums.index(combination[0])].update({'score': combination[0]['score'] + 1})
        elif answer == '2':
            albums[albums.index(combination[1])].update({'score': combination[1]['score'] + 1})
        else:
            print('Skipping...')

    print('')
    sorted_albums = sorted(albums, key = lambda i: i['score'], reverse = True)
    for i in range(5):
        print(str(i+1) + '. ' + sorted_albums[i]['title'] + ' (' + str(sorted_albums[i]['score']) + 'p)')