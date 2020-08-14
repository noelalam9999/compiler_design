def checkPattern(string, pattern): 
  
    
    l = len(pattern) 
  
  
    if len(string) < l: 
        return False
  
    for i in range(l - 1): 
  
        
        x = pattern[i] 
        y = pattern[i + 1] 
  
        last = string.rindex(x) 
        first = string.index(y) 
        
        if last == -1 or first == -1 or last > first: 
            return False
  
    
    return True
def parser(): 
    f = open("two.txt","r")
    for word in f:
        a=0
        b=0
        c=0
        if checkPattern(word,"abcde")==True:
            for letter in word:
                    
                if letter == "a" or letter == "b":
                    if letter == "a":
                        a+=1
                    else:
                        a-=1
                elif letter == "c":
                    c+=1
                elif letter == "d" or letter == "e":
                    if letter == "d":
                        b+=1
                    else:
                        b-=1
                else: 
                    if letter.isspace()==True:
                        pass
                    else:
                        print("unknown word")    
            if a!=0 or b!=0 or c!=1:
                print(word," cannot be parsed")
            else: 
                print(word," parsed")   
        else: 
            print(word,"cannot be parsed")     


parser()
    

