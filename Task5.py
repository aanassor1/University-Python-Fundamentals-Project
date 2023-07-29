def check_word_tiles(word, myTiles): #The functino to check if the word can be made with the tiles
    if word.isalpha() == True: #Check if it is a word
        can_be_made = True
        for x in word: #Loop over the characters of the string
            found = False
            for y in myTiles: #Loop over the myTiles list
                if x == y: #If the character is the same as one of the characters in the myTiles List
                    found = True #Change the boolean, remove the entry from the list and break
                    myTiles.remove(y)
                    break
            if found == False: #If the code went over the entire list and Found is still false, then we can assume the word cannot be made with the tiles.
                can_be_made = False
                break
        print(can_be_made) #Print whether you can make the word or not

check_word_tiles("SWET", ['T','Y','S','E','U','W','I'])