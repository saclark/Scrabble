##
##
##    letters = input('What are your scrabble letters: ')
##
##    if letters in open('words.txt').read():
##            print ('true')
##    else:
##            print ('false')
##        


##def get_letters():
##    letters = input('what are your letters: ')
##    print letters 
##    
##get_letters()



def get_list(filepath):
    return open(filepath).read()

print (get_list('words.txt'))
