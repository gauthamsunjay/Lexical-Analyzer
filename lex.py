from lexer import *
import prettytable as pt

def readProgram(filename):
    prog = []
    lineNum = 0
    with open(filename) as f:
        data = f.read()
    
    i = 0
    temp = []
    while(i<len(data)):
        if(data[i]=='/' and data[i+1]=='/'):
            while(data[i]!='\n'):
                i += 1

            if(data[i]=='\n'):
                lineNum += 1
   
        
        if(data[i]=='/' and data[i+1]=='*'):
            while(True):
                if(data[i]=='\n'):
                    lineNum += 1

                if(data[i]=='*' and data[i+1]=='/'):
                    i += 2
                    break

                i += 1    

        
        temp.append(data[i])
        if(data[i]=='\n'):
            lineNum += 1
            temp = "".join(temp).split('\n')[0]
            temp = temp.strip()
            tup = (temp,lineNum)
            prog.append(tup)
            temp = []
        
        i += 1

    return prog


filename = input("Enter filename: ")
prog = readProgram(filename) #remove comments from the program


prog = removePPD(prog)

for line in prog:
    if(line[0]!=''):
        identifiers(line)
        operator(line)
        spSymbols(line)
        strings(line)
        constants(line)



x = pt.PrettyTable(["Line","Lexeme","Token","Span"],align='c')
for i in tokens:
    x.add_row([i[0],i[1],i[2],i[3]])

print(x)




