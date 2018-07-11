import random
wordlist = list()



print("Welkom bij Galgje! Raad het woord en win een prijs! (of niet)")

level = input("Kies een niveau. 1 is een lengte van 6 tot en met 10, 2 is van 11 tot en met 15 en 3 is alles daarboven.")

listfile = open("files/newdutch.txt")
for line in listfile:
    line = line.rstrip()
    if level == str(1):
        if  6 <= len(line) <= 10:
            wordlist.append(line)
    if level == str(2):
        if 11 <= len(line) <= 15:
            wordlist.append(line)
    if level == str(3):
        if len(line) > 15:
            wordlist.append(line)

randomint = random.randint(0, len(wordlist) - 1)

chosenword = wordlist[randomint]

turns = len(chosenword) + len(chosenword)/1.25
newround = int(round(turns))



print("De lengte van het woord is: " +  str(len(chosenword)))

print ("Je hebt " + str(newround) + " beurten om het woord te raden!")

print("* " * len(chosenword))
print("_ " * len(chosenword))
turncount = 0
foundletters = list()

while turncount <= newround:
    foundcount = 0
    letter = input("Kies een letter: ")
    if len(letter) == 1 and letter not in foundletters:
        if letter in chosenword:
            print("Goed gevonden!")
            foundletters.append(letter)
            for letters in chosenword:
                if letters in foundletters:
                    print(letters + " ", end="")
                    foundcount = foundcount + 1
                else:
                    print("_ ", end="")

            #print(foundletters)
        else:
            print("Helaas, probeer een andere letter")
            print("\n Je hebt nog " + str(newround - turncount) + " beurten over!")
            turncount += 1

    elif len(letter) != 1:
        print("Voer maximaal 1 letter in!")
    elif letter in foundletters:
        print("Deze letter heb je al gekozen, kies een andere.")
    if turncount == newround+1:
        print("Helaas, het spel is voorbij!")
        print("Het woord was: " + chosenword)
        print("Het woord wordt gekozen uit een grote lijst, als je denkt dat er iets mis is of dit woord er niet in thuis hoort, neem dan contact op.")
        input("Druk op Enter om af te sluiten...")
    if foundcount == len(chosenword):
        print("Gefeliciteerd, je hebt gewonnen!")
        break