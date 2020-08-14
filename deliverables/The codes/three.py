class i_to_p_conversion:
    precedence={'+':4,'-':3,'*':2,'/':2}
    def __init__(self):
        self.stack=[]
        self.size=-1
    
    def top(self):
        if self.size==-1:
            return False
        else:
            return self.stack[self.size]
  
    
    
    def push(self,value):
        self.stack.append(value)
        self.size+=1
    def pop(self):
        if self.size==-1:
            return 0
        else:
            self.size-=1
            return self.stack.pop()
    
    
    def convert(self,expr):
        postfix=""
        
        for i in expr:
            if(len(expr)%2==0):
                print("please enter a proper infix expression")
                return False
            elif(i.isalnum()):
                postfix +=i
            elif(i in '+-*/'):
                while(len(self.stack) and self.precedence[i]<=self.precedence[self.top()]):
                    postfix+=self.pop()
                self.push(i)
          
        while len(self.stack):
            postfix+=self.pop()


        return postfix


f = open("three.txt","r")
for string in f:
    s=i_to_p_conversion()
    postfix = s.convert(string)
    print(postfix) 