# Task 1. Function that return 'Hello!'

#function that returns string "Hello!"
def hello():
    return 'Hello!'

#output function result
# print(hello())

# Task 2: Greet with a Formatted String

#Function that greet person using the name
#name: string - the name of the person for greeting
def greet(name):
    return f"Hello, {name}!"

#output function result
# print(greet('Mike'))

# Task 3: Calculator

#Function that provide basic math operations
#arg1: int or float - first argument in operation
#arg2: int or float - second argument in operation
#operation: string  - operation defenition ( by default : multiply)
def calc(arg1, arg2, operation = 'multiply'):
    #assign the result of operation 0
    result = 0
    try:
        #check if arguments that passed through the function are numbers. If not - rais the TypeError exception
        if not (type(arg1) == int  or type(arg1) == float):
            raise TypeError("arg1")
        if not (type(arg2) == int or type(arg2) == float):
            raise TypeError("arg2")
        #do the operation
        match operation:
            case 'add':
                result = arg1 + arg2
            case 'subtract':
                result = arg1 - arg2
            case 'multiply':
                result = arg1 * arg2
            case 'divide':
                result = arg1 / arg2
            case 'modulo':
                result = arg1 % arg2
            case 'int_divide':
                result = arg1 // arg2
            case 'power':
                result = arg1 ** arg2
            case _:
                #default case, if operation parameter is unexpected string
                raise ValueError('Unexpected type of operation!')
    except TypeError as e:
        return f"You can't {operation} those values!"
    except ZeroDivisionError as e:
        return f"You can't divide by 0!"
    except ValueError as e:
        return f"{e}"
    else:
        #if there is no exceptions raised - return the result of calculation        
        return result

    
#output function result
# print(calc(5,6))
# print(calc(7,6,'add'))
# print(calc("7",6,'add'))
# print(f"Case, when only manual type check show the error: {calc(7,True,'add')}")
# print(calc(5,6,'subtract'))
# print(calc(5,6, 'divide'))
# print(calc(5,0, 'divide'))
# print(calc(7,6, 'modulo'))
# print(calc(7,6,'int_divide'))
# print(calc(5,6,'power'))

#Task 4: Data Type Conversion

#function that convert value to the specific type
#value: any - value that need to convert
#type_name: string - the name of the type
def data_type_conversion(value, type_name):
    try:
        #chose type according to the type name
        match type_name:
            case "int":
                result = int(value)
            case "float":
                result = float(value)
            case "str":
                result = str(value)
            case _:
                #raise exception if type_name is different as expected
                raise ValueError('Type name is wrong')
    except ValueError as e:
        if e == 'Type name is wrong':
            return f'Unexpected type of operation! Type is {type_name}.'
        return f"You can't convert {value} into a {type_name}."
    else:
        #if there is no error in conversion - return the result
        return result 
    
#output function result
# print(data_type_conversion(1, "float"))
# print(data_type_conversion(1.1, "int"))
# print(data_type_conversion(11, "str"))
# print(data_type_conversion("11", "int"))
# print(data_type_conversion("2.2", "float"))
# print(data_type_conversion("ab", "int"))

#Task 5: Grading System, Using *args

#function that calculate average grade result
#arg: int - list of scores
def grade(*arg):
    try:
        #try to calculate averate score amount
        average_score = sum(arg)/len(arg)
    except TypeError:
        #in case if provided invalid argument - string instead of numbers
        return f"Invalid data was provided."
    else:
        #if average score was calculated return the student final score
        if average_score >= 90:
            return "A"
        elif average_score >=80 and average_score <=89:
            return "B"
        elif average_score >=70 and average_score <=79:
            return "C"
        elif average_score >=60 and average_score <=69:
            return "D"
        else:
            return "F"
        
#output function result
# print(grade(90,98,89))
# print(grade(90,98,50,80))
# print(grade(90,"A",89))
# print(grade("90","98","89"))

#Task 6: Use a For Loop with a Range

#function that repeat string
#string: any - sourse data
#count: number - amount of repetitions
def repeat(string,count):
    try:
        string = str(string)
        result_string = ""
        for i in range(count):
            result_string += string
        return result_string
    except TypeError:
        return f"Count should be a number!"

#output function result
# print(repeat('AB',3))
# print(repeat(12,5))
# print(repeat(12,"AB"))


#Task 7: Student Scores, Using **kwargs

def student_scores(score_type, **kwargs):
    try:
        match score_type:
            case "mean":
                #calculate the average score of the group
                result = sum(kwargs.values())/len(kwargs)
            case "best":
                max_score = -1
                for student, score in kwargs.items():
                    if score > max_score:
                        max_score =score
                        result = student
            case _:
                #raise exception if score_type is different as expected
                raise ValueError('You trying to get wrong type of scores!')
    except ValueError as e:
        return f"{e}"
    except TypeError:
        return 'Scores should be a numbers!'
    else:
        return result

#output function result
# print(student_scores("mean", Alex=90, Ben=60, Lana =90, Eva = 70, Mike = 95 ))
# print(student_scores("best", Alex=90, Ben=60, Lana =90, Eva = 70, Mike = 95 ))
# print(student_scores("average", Alex=90, Ben=60, Lana =90, Eva = 70, Mike = 95 ))
# print(student_scores("mean", Alex=90, Ben="60", Lana =90, Eva = 70, Mike = 95 ))

#Task 8: Titleize, with String and List Operations

#Function that capitalized the string according to the boog title rules
def titleize(title):
    #create a set of exceptional words that should not be capitalized
    lowercase_words = { "a", "on", "an", "the", "of", "and", "is", "in"}
    #create a list of words from title string
    title_words = title.split(" ")
    #counr amount of words
    words_amount = len(title_words)
    #loop through the words
    for index in range(words_amount):
        word = title_words[index]
        #if there is not first or last words, and not a word from exception list, then capitalize it
        if not word in lowercase_words or index == 0 or index == words_amount -1 :
            title_words[index] = word.capitalize()
    #returned the title as a string        
    return " ".join(title_words)

#output function result
# print(titleize("harry potter and the chamber of secrets"))
# print(titleize("the beauty and the beast"))
# print(titleize("the secret of town a"))

#Task 9: Hangman, with more String Operations
 
 #function that emulate hangman
 #secret: string - word that the caller doesn't know
 #guess: string - letters that the caller is trying to guess
def hangman(secret,guess):
    #as we do not pay attention on upper or lower case in letters - change all to lowercase
    secret = secret.lower()
    guess = guess.lower()
    #create a set from guess letters
    guess_letters = set(guess)
    #calculate the length of secret word
    secret_length = len(secret)
    #create a result list of characters, by default - "_"
    result_letters = ["_"]*secret_length
    #loop through letters in secret word
    for index in range(secret_length):
        #if current letter is in guess set - add it to result list
        if secret[index] in guess_letters:
            result_letters[index] = secret[index]
    #return result as a string
    return "".join(result_letters)


#output function result
# print(hangman("elephant", "es"))
# print(hangman("elephant", "EL"))

#Task 10: Pig Latin, Another String Manipulation Exercise
#function that convert text to pig latin
#text:string - text that would be converted
def pig_latin(text):
    #convert text to lowercase to prevent errors related to the case sensitive information
    text = text.lower()
    #declare the result list of converted words
    pig_latin_list = []
    #split the string to list of words
    words_list = text.split()
    #declare the set of vowels
    vowels = {"a","e","i","o","u"}
    #loop through the all words in text and conver them according to the rules
    for word in words_list:
        #find the letters that have to be moved to the end of the word
        #index of the letter in word
        index = 0
        #the first letter that could be moved
        letter = word[index]
        #suffix that would be added to the end of the word
        pig_suffix = ""
        #loop throug the letters until we don't fins the vowel
        while letter not in vowels and index<len(word):
            #add current consonant letter to suffix
            pig_suffix += letter
            index += 1
            letter = word[index]
        #check the specific case if we have 'qu' consequence of lettes
        if len(pig_suffix) > 0 and pig_suffix[-1] == "q" and word[index] == "u":
            pig_suffix += "u"
            index +=1
        #add 'ay' as obliged ending of each word
        pig_suffix += "ay"
        #add new word in our pig latin word list (take the rest of current word and add to it our suffix)
        pig_latin_list.append(word[index:] +pig_suffix)
    #return result as a string
    return " ".join(pig_latin_list)

#output function result
# print(pig_latin('i like apples and bananas this is the main question'))
# print(pig_latin('cherry'))
# print(pig_latin('that'))
# print(pig_latin('strawberry'))

