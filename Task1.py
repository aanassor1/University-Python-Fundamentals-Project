ScoresFile = open(r"D:\Documents\Uni\Year 1\Programming\Assignment\scores.txt", "r") #open the score file
ScoresList = [] #the score list
for x in ScoresFile: #Read the entire file line by line and then add the line into the corresponding list.
  ScoresList.append(x)
ScoresFile.close() #Close the score file

DictionaryFile = open(r"D:\Documents\Uni\Year 1\Programming\Assignment\dictionary.txt", "r") #open the dictionary file
DictionaryList = [] #the dictionary list
for x in DictionaryFile: #Read the entire file line by line and then add the line into the corresponding list.
  DictionaryList.append(x)
DictionaryFile.close() #Close the dictionary file

TilesFile = open(r"D:\Documents\Uni\Year 1\Programming\Assignment\tiles.txt", "r") #open the tiles file
TilesList = [] #the tiles list
for x in TilesFile: #Read the entire file line by line and then add the line into the corresponding list.
  TilesList.append(x)
TilesFile.close() #Close the tiles file