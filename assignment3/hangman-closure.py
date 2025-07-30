
#Task 4: Closure Practice

def make_hangman(secret_word):
    secret_word = secret_word.lower()
    guesses =[]
    word_length = len(secret_word)
    result = ["_" for _ in range(word_length) ]
    def hangman_closure(letter):
        letter = letter.lower()
        guesses.append(letter)
        for index in range(word_length):
            if secret_word[index] == letter:
                result[index] = letter
        word = "".join(result)
        print(word)
        if word == secret_word:
            return True
        return False
    return hangman_closure

game = make_hangman("tRee")

game("T")
print(game("r"))
game("e")


