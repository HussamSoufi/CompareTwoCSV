with open('old.csv', 'r') as t1, open('new.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    outFile.write("new stuff to add \n")
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)

    outFile.write("\n \n \n")

    outFile.write("old stuff to delete \n")
    for line in fileone:
        if line not in filetwo:
            outFile.write(line)
