ScoresFile = open(r"D:\Documents\Uni\Year 1\Programming\Assignment\scores.txt", "r") #open the score file
ScoresDictionary = {} #the score dictionary
for x in ScoresFile: #Read the entire file line by line and then add the line into the corresponding list.
  score_letter = x.split()[0].lower() #The score letter
  score_score = x.split()[1] #The score of the letter
  ScoresDictionary[score_letter] = score_score #Input it in the dictionary
ScoresFile.close() #Close the score file

def getLetterScore(Letter): #Return the score of the letter
    if len(Letter) == 1: #Make sure the letter is only length 1
        is_letter = Letter.isalpha()
        if is_letter == True: #Check if its a letter
            return ScoresDictionary.get(Letter.lower()) #Return the score of the letter

user_input_letter = input("Please enter a letter: ") #Ask the user to input a letter
print(getLetterScore(user_input_letter)) #Get the result of the score of the letter