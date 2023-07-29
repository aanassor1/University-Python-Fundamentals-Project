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
    DictionaryList.append(x.lower()[0:len(x)-1])
DictionaryFile.close() #Close the dictionary file

def getLetterScore(Letter): #Return the score of the letter
    if len(Letter) == 1: #Make sure the letter is only length 1
        is_letter = Letter.isalpha()
        if is_letter == True: #Check if its a letter
            return ScoresDictionary.get(Letter.lower()) #Return the score of the letter

def checkWord(Word):
    if Word.isalpha() == True:  # Check if its a word
        is_found = False
        for x in DictionaryList: #Loop through the list to check if the word exists
            if x == Word.lower():
                is_found = True
        return(is_found) #Return the status

user_input_word = input("Please enter a word: ") #Ask the user to input a word
if checkWord(user_input_word) == True: #If the word is in the dictionairy, proceeed to find the score
    TotalScore = 0
    for character in user_input_word: #Loop through over the characters of the string and add to total score
        TotalScore = TotalScore + int(getLetterScore(character))
    print(TotalScore) #Print it