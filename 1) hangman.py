import random


words_bank = ["tree", "book", "blue", "train", "fish", "woman", "life", "freedom", "iran", "sky"]
user_mistakes = 0

right_chars = []
wrong_chars = []

x = random.randint (0, len(words_bank)-1)
word = words_bank [x]    #instead of lines 5 & 6, you can write: word = random.choice (words_bank)

while user_mistakes < 6:
    for i in range (len(word)):
        if word[i] in right_chars:
            print (word[i], end=" ")
        else:
            print ("_", end=" ")

    if len (right_chars) == len (set (word)) :
        print ("You won.")
        print ("🔴🟠🟡🟢🔵🟣")
        break
    
    user_char = input ("please write your guess: ").lower()
    if len(user_char) == 1:
        if user_char in word:
            right_chars.append(user_char)
            print ("✅")
        else:
            wrong_chars.append(user_char)
            user_mistakes = user_mistakes + 1
            print ("❌")
    else:
        print ("Enter only 1 letter!")

if user_mistakes == 6:
    print ("Game Over!")