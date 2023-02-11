#!/usr/bin/python3
import random

# wordle solver

# returns a random word from words (the dictrionary)
def getRandomWord(words) :
    size = len(words)
    return words[random.randint(0,size-1)]

def index_of(list,value):
    for i in range(len(list)):
        if list[i] == value:
            return i;
    return -1
    
def changeLetterToSpaceInWord(word,pos):
    new_word = ""
    i = 0
    for ch in word:
        if (i == pos):
            new_word = new_word + ' '
        else:
            new_word = new_word + ch
            i = i + 1
            return new_word
            
# Evaluates guess:  assigns 5-element list, guessEvalution
# 0 = invalid Letter
# 1 = right letter, wrong place
# 2 = right letter, right place
def evaluate_guess(guess, words, the_word):
    guess_list = list(guess)
    the_word_list = list(the_word)
    evaluation = [0,0,0,0,0]
    i = 0
    # Look for # 2 = right letter, right place
    for i in range(5):
        if guess_list[i] == the_word_list[i]:
            evaluation[i] = 2
            guess_list[i] = ' '
            the_word_list[i] = ' '
            
    # Look for # 1 = right letter, wrong place
    for i in range(5):
        if evaluation[i] == 0:
            index = index_of(the_word_list,guess[i])
            if index != -1:
                evaluation[i] = 1
                guess_list[i] = ' '
                the_word_list[index] = ' '
    return evaluation

# Returns True if string, str has any of the char in chars list
def string_has_any_of(str, chars):
    for ch in chars:
        if ch in str:
            return True
    return False

        			
def wordMatchesPattern(guess, pattern, words):
    temp_words = []
    
    # Check pattern string for 0s
    for i in range(0,5):
        if pattern[i] == 0:
            for word in words:
                if word[i] != guess[i]:
                    temp_words.append(word)
        if len(temp_words) > 0:
            words = temp_words
            temp_words = []
    if guess == "stave":
        print("63:",words)
                                    
    # Check pattern string for 2s
    for i in range(0,5):
        if pattern[i] == 2:
            for word in words:
                if word[i] == guess[i]:
                    if word not in temp_words:
                        temp_words.append(word)
        if len(temp_words) > 0:
            words = temp_words
            temp_words = []
                    	
    # Check pattern string for 1s
    for i in range(0,5):
        if pattern[i] == 1:
            for word in words:
                if guess[i] in word and guess[i] != word[i]:
                    if word not in temp_words:
                        temp_words.append(word)
        if len(temp_words) > 0:
            words = temp_words
            temp_words = []                    	
    return words

 
wordfile = "/media/joe/E_drive/software/sfml/wordle/resources/wordfile.txt"
words = []
counter = 0
temp_words = []
game_over = False
guesses = 0

try:
    with open(wordfile) as fin:
        for word in fin:
            words.append(word.rstrip())
        fin.close()
            
    the_word = getRandomWord(words)
    #the_word = "error"
    the_word = "stage"

    while not game_over:
        guesses += 1
        if (guesses > 6):
            print("Too bad!  You lose.")
            break
        guess = getRandomWord(words)
        #if (guesses == 1):
        #    guess = "earth"
        print("Guess #",guesses,"the_word=",the_word,"  guess=",guess)
        if (guess == the_word):
            game_over = True
            print("You win!!!  And it only took you",guesses,"guesses.")
            break
                    
        pattern = evaluate_guess(guess,words,the_word)
        print("Evaluation:",pattern)
        words = wordMatchesPattern(guess,pattern,words)
        if guess in words:
            words.remove(guess)
        print("Number of words left to choose from",len(words))
        if (len(words) < 34):
            print(words)
        print("")

except Exception as e:
    print("Unable to open file",wordfile)
