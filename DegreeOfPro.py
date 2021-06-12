

slur1 = ['nigger', 'Bihari',]
slur2 = []
slur3 = []

def isFound(slur, word):
    result  = word in slur
    return result

tweet = input("Enter tweet for which you want know profanity level : ")
word = tweet.split()

for i in range(0, len(word)):
    if(isFound(slur1, word[i])):
        print("Level 1")
        break;
    elif(isFound(slur2, word[i]):
         print("level 2")
         break;
    elif(isFound(slur3, word[i]):
         print("Level 3")
         break
    else:
        print("No profanity")
    
