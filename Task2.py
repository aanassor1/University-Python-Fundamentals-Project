def onlyEnglishLetters(word): #This function returns if the word is english only or not
    is_english = True #A boolean to check if the word is true
    for theCharacter in word: #Loop over the characters of the word
        letter_is_english = theCharacter.isalpha() #A function to check if the character is english
        if letter_is_english == False: #If the character is not english
            is_english = False #change the is_english boolean value to false and stop the loop
            break
    return is_english #Return if the word is true or false

user_input_word = input("Please enter a word: ") #Ask the user to input the word
print(onlyEnglishLetters(user_input_word)) #Return the value of the function