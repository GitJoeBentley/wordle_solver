# wordle solver

def wordMatchesPattern(guess, pattern,words):
    temp_words = []

    # Check pattern string for 0s
    exclude = ""
    for i in range(0,5):
        if pattern[i] == 0:
            exclude = exclude + guess[i]

    for ch in exclude:
        for word in words:
            if ch not in word:
                temp_words.append(word)
        if len(temp_words) > 0:
            words = temp_words
        temp_words = []     

    print("line 19:",len(words))              

    # Check pattern string for 2s
    for i in range(0,5):
        print("23:",i," len(words)=",len(words))
        if pattern[i] == 2:
            for word in words:
                if word[i] == guess[i]:
                    temp_words.append(word)
            if len(temp_words) > 0:
                words = temp_words
            temp_words = []
        print("30:",i," len(words)=",len(words))


    print("line 33:",len(words))        
    for word in words:
        print("***",word)

    # Check pattern string for 1s
    for i in range(0,5):
        if pattern[i] == 1:
            for word in words:
                if guess[i] in word:
                    temp_words.append(word)
        if len(temp_words) > 0:
            words = temp_words
        temp_words = []
    
    return words

wordfile = "E:/software/sfml/wordle/resources/wordfile.txt"

words = []
counter = 0
temp_words = []

with open(wordfile) as fin:
    for word in fin:
        words.append(word.rstrip())
    fin.close()

print(len(words))
pattern = [1,1,0,2,0]
words = wordMatchesPattern("inate",pattern,words)
print(len(words))
for word in words:
    print(word)

