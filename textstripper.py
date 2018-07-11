#with open('dutch.txt', encoding="utf8") as f:
    #content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
#lines = [line.split("/")[0] for line in open('dutch.txt', encoding="utf8")]

dictfile = open("dutch.txt", encoding='utf8')
newfile = open("newdutch.txt", 'w' , encoding='utf8')
for line in dictfile:

    line = line.split("/")[0]
    line = line.lower()
    if "-" not in line and "'" not in line and len(line) > 6 and "Ä" not in line and "ä" not in line:
        if "\r" in line or "\n" in line:
            newfile.write(line)
        else:
            newfile.write(line + "\n")