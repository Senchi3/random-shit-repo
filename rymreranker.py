# Only albums with this RYM score and higher get selected
min_score = 10

with open("data/input.txt", 'r', encoding="utf-8") as infile, \
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

        # filter out albums with bad scores
        rym_score = 0 if line_elements[7] == '' else int(line_elements[7])
        if rym_score < min_score:
            continue

        formatted_line = "{} {} {} {} - {} ({})".format(line_elements[1],
                                                         line_elements[2],
                                                         line_elements[3],
                                                         line_elements[4],
                                                         line_elements[5],
                                                         line_elements[6])
        albums.append(formatted_line)

    # bubble sort algorithm
    # couldnt figure out how to reverse it so it just reverses the list after sorting
    for i in range(len(albums)):
        swapped = False
        for j in range(len(albums)-i-1):
            print('\nA:', albums[j])
            print('B:', albums[j+1])
            answer = input("Which album is better? (A/B) ")

            if answer.lower().rstrip() == 'a':
                albums[j], albums[j+1] = albums[j+1], albums[j]
                swapped = True
        if swapped == False:
            break
    albums.reverse()

    print('')
    for i in range(5):
        print('{}. {}   ({}p)'.format(i+1, albums[i], albums[i]))