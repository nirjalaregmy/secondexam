def findletter(word,letter):
    isthere = 'no'               
    for i in range(0,len(word)):  
        if(letter == word[i]):
            isthere = 'yes'
    if(isthere ==  'yes'):
        print("present")
    elif(isthere == 'no'):
        print("absent")
 
findletter("arnab",'a')  
