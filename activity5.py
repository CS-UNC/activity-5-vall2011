#words_file = open ('CROSSWD.txt','r')

#print(type (words_file))
#for line in words_file:
    #print(line.strip())
    #print (line)
    #words.append(line)

#print(words)
#print([x for x in dir(words_file) if '_' != x[0]])
#while True:
    #print(words_file.readline())clear

#print(words_file.readline())
#data=[1,3,2,8,5,6,10]
#print([2*x for x in data if x % 2 == 0])
def more_than_20(file):
    words= []
    data = open(file, 'r')
    #for word in data:
        #if len(word.strip()) > 20:
            #words.append(word.strip())
    #return words   
    words = [x.strip() for x in data if len(x.strip())> 20]
    return words
print(more_than_20("CROSSWD.txt"))


def has_no_e (word):
    if 'e' in word:
        return False
    else:
        return True
    
def uses_only(word,letters):
    for x in word:
        if x not in letters:
            return False
    
    return True

def all_uses_only(file, letters):
    for letters in file:
        uses_o = uses_only(word,letters)
        if uses_o == True:
            return letters


#check = True
#for letter in word:
    #if 'e' == letter:
        #check=False
#return check

