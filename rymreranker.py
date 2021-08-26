import re

with open("data/rym.txt", 'r', encoding="utf-8") as infile, \
     open("data/output.txt", 'w', encoding="utf-8") as outfile, \
     open("data/filter.txt", 'r', encoding="utf-8") as filterfile:
    
    # Data preparation

    filters = filterfile.readlines()
    lines = infile.readlines()
    data = [[]]
    count = 0
    newlines = []

    # Data filter

    for line in lines:
        for filter in filters:
            if filter in line:
                break
            else:
                count =+ 1
                if count <= len(filters):
                    newlines.append(line)
                    break



    print("HERE ARE THE NEWLINES")
    print(newlines)
    print("NO MORE NEWLINES")

    # Data formatting

    for line in newlines:
        # RYM Album, First Name,Last Name,First Name localized, Last Name localized,Title,Release_Date,Rating,Ownership,Purchase Date,Media Type,Review
        count += 1
        print("Line #{} was: {}".format(count, line))
        line = line.replace("\"", "")
        print("Line #{} is now: {}".format(count, line))
        line = line.split(",")
        currentdata = "{} {} {} {}  - {} ({})".format(line[1],line[2],line[3],line[4],line[5],line[6])
        print("Line #{} has been formatted as: {}".format(count, currentdata))
        data.append([currentdata, 0])
    
    n = len(data)


    # NOTE: FROM HERE ON OUT BASICALLY EVERYTHING IS BROKEN

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-2):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # RYM Album, First Name,Last Name,First Name localized, Last Name localized,Title,Release_Date,Rating,Ownership,Purchase Date,Media Type,Review
            firstoption = data[j + 1]
            secondoption = data[(j + 2)]
            print(firstoption)
            print(secondoption)
            opinion = int(input("Which one of these is better: (1) {} or (2) {}?".format(firstoption[0], secondoption[0])))
            if opinion == 1:
                data[j][1] = opinion
            elif opinion == 2:
                data[j + 1][1] = opinion