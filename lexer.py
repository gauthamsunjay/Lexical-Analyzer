import re
'''
functions for the tokens

'''
keywords = ['auto','break','case','char','double','else','enum','extern','int','long','register','return','struct','switch','typedef','union','const','continue','default','do','float','for','goto','if','short','signed','sizeof','static','unsigned','void','volatile','while']

tokens = []

def operator(line):
    string,lineNum = line
    r = re.finditer(r"\+\+|\-\-|<=|>=|[\+\*=/\-%&><]",string)
    m = re.findall(r"\".*\"",string)
    for i in r:
        if m:
            flag = 0
            for j in m:
                if i.group() in j:
                    flag = 1
            
            if flag==0:
                tup = (lineNum,i.group(),'OP',i.span())
                tokens.append(tup)

        else:
            tup = (lineNum,i.group(),'OP',i.span())
            tokens.append(tup)

def identifiers(line):
    string,lineNum = line
    l = re.finditer(r"[_a-zA-Z]\w*",string)
    m = re.findall(r"\".*\"",string,re.DOTALL)
    for i in l:
        if m:
            flag = 0
            for j in m:
                if i.group() in j:
                    flag = 1
                    
            if flag==0:
                if i.group() in keywords:
                    tup = (lineNum,i.group(),'KEYWORD',i.span())
                    tokens.append(tup)

                else:
                    tup = (lineNum,i.group(),'ID',i.span())
                    tokens.append(tup)
        
        else:
            if i.group() in keywords:
                tup = (lineNum,i.group(),'KEYWORD',i.span())
                tokens.append(tup)

            else:
                tup = (lineNum,i.group(),'ID',i.span())
                tokens.append(tup)
    
def spSymbols(line):
    string,lineNum = line
    r = re.finditer(r"[\[\]\(\)\{\};,]",string)
    m = re.findall(r"\".*\"",string)
    for i in r:
        if m:
            flag = 0
            for j in m:
                if i.group() in j:
                    flag = 1
            
            if flag==0:
                tup = (lineNum,i.group(),'SPLSYM',i.span())
                tokens.append(tup)
         
        else:
            tup = (lineNum,i.group(),'SPLSYM',i.span())
            tokens.append(tup)


def strings(line):
    string,lineNum = line
    r = re.finditer(r"\".*\"|\'.*\'",string)
    for i in r:
        tup = (lineNum,i.group(),"STRING",i.span())
        tokens.append(tup)


def constants(line):
    string,lineNum = line
    r = re.finditer(r"\s*(\d+|\d*\.\d+)[,;\b]?",string)
    m = re.findall(r"\".*\"",string)
    for i in r:
        if m:
            flag = 0
            for j in m:
                if i.group(1) in j:
                    flag = 1
            
            if flag==0:
                tup = (lineNum,i.group(1),"CONST",i.span())
                tokens.append(tup)

        else:
            tup = (lineNum,i.group(1),"CONST",i.span())
            tokens.append(tup)

    
def removePPD(prog):
    ppd = []
    for i in prog:
        j,k = i
        r = re.fullmatch(r"(#.*<.*>|#.*\s*\".*\")",j)
        if r:
            ppd.append(i)
            
    for i in ppd:
        prog.remove(i)
        
    return (prog)

