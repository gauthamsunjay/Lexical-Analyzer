from lexer import *

def readProgram(filename):
    prog = []
    with open(filename) as f:
        data = f.read()
    
    i = 0
    temp = []
    while(i<len(data)):
        if(data[i]=='/' and data[i+1]=='/'):
            while(data[i]!='\n'):
                i += 1
   
        
        if(data[i]=='/' and data[i+1]=='*'):
            while(True):
                if(data[i]=='*' and data[i+1]=='/'):
                    i += 2
                    break

                i += 1    

        
        temp.append(data[i])
        if(data[i]=='\n'):
            prog.append("".join(temp))
            temp = []

        i += 1

    return prog


filename = input("Enter filename: ")
prog = readProgram(filename) #remove comments from the program
prog = "".join(prog).split('\n')


for i in range(len(prog)):
   prog[i] = prog[i].strip()

while '' in prog:
   prog.remove('')


prog = removePPD(prog)

for line in prog:
    operator(line)
    identifiers(line)
    spSymbols(line)
    strings(line)
    constants(line)

for i in tokens:
    print(i)

