
#Task 4: Closure Practice

#function for hangman game
def make_hangman(secret_word):
    #change the secret to lowercase
    secret_word = secret_word.lower()
    #set the list of guesses
    guesses =[]

    word_length = len(secret_word)
    #list of letters to print out the result of game
    result = ["_" for _ in range(word_length) ]

    def hangman_closure(letter):
        #convert letter for lowercase
        letter = letter.lower()
        #add guess to list
        guesses.append(letter)
        #search letter in word
        for index in range(word_length):
            if secret_word[index] == letter:
                #add existing letter to resule list
                result[index] = letter
        #convert list to string
        word = "".join(result)
        ##print out result
        print(word)
        #check if secret was uncovered
        if word == secret_word:
            return True
        return False
    return hangman_closure

#input the secret word
secret = input("Enter you secret word: ")
#declare a game
game = make_hangman(secret)
#declare flag for game steps
is_solved = False
#continue input letters
while not is_solved:
   #input the letter
   letter = input("Enter your letter: ")
   #make turn
   is_solved = game(letter)
   #check the result to print info
   if is_solved:
      print("You finish the game!")
       




