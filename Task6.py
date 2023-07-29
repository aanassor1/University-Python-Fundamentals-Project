ScoresFile = open(r"D:\Documents\Uni\Year 1\Programming\Assignment\scores.txt", "r") #open the score file
ScoresDictionary = {} #the score dictionary
for x in ScoresFile: #Read the entire file line by line and then add the line into the corresponding list.
  score_letter = x.split()[0].lower() #The score letter
  score_score = x.split()[1] #The score of the letter
  ScoresDictionary[score_letter] = score_score #Input it in the dictionary
ScoresFile.close() #Close the score file

DictionaryFile = open(r"D:\Documents\Uni\Year 1\Programming\Assignment\dictionary.txt", "r") #open the dictionary file
DictionaryList = [] #the dictionary list
for x in DictionaryFile: #Read the entire file line by line and then add the line into the corresponding list.
    DictionaryList.append(x.upper()[0:len(x)-1])
DictionaryFile.close() #Close the dictionary file

def getLetterScore(Letter): #Return the score of the letter
    if len(Letter) == 1: #Make sure the letter is only length 1
        is_letter = Letter.isalpha()
        if is_letter == True: #Check if its a letter
            return ScoresDictionary.get(Letter.lower()) #Return the score of the letter

def checkWord(Word, dictionary): #Check if the word is in the dictionary
    if Word.isalpha() == True:  # Check if its a word
        is_found = False
        for x in dictionary: #Loop through the list to check if the word exists
            if x == Word.upper():
                is_found = True
        return is_found #Return the status

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
        return can_be_made #Print whether you can make the word or not

def isValid(word, myTiles, dictionary):
    status = False
    if checkWord(word, dictionary) == True:  # If the word is in the dictionairy, proceeed to find the score
        if check_word_tiles(word, myTiles) == True: #If the word can be made with the tiles, return True
            status = True
    return status