import re
'''
functions for the tokens

'''
keywords = ['auto','break','case','char','double','else','enum','extern','int','long','register','return','struct','switch','typedef','union','const','continue','default','do','float','for','goto','if','short','signed','sizeof','static','unsigned','void','volatile','while']

tokens = []

def operator(string):
    r = re.finditer(r"\+\+|\-\-|<=|>=|[\+\*=/\-%&><]",string)
    m = re.findall(r"\".*\"",string)
    for i in r:
        if m:
            flag = 0
            for j in m:
                if i.group() in j:
                    flag = 1
            
            if flag==0:
                tup = (i.group(),'OP')
                tokens.append(tup)

        else:
            tup = (i.group(),'OP')
            tokens.append(tup)

def identifiers(string):
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
                    tup = (i.group(),'KEYWORD')
                    tokens.append(tup)

                else:
                    tup = (i.group(),'ID')
                    tokens.append(tup)
        
        else:
            if i.group() in keywords:
                tup = (i.group(),'KEYWORD')
                tokens.append(tup)

            else:
                tup = (i.group(),'ID')
                tokens.append(tup)
    
def spSymbols(string):
    r = re.finditer(r"[\[\]\(\)\{\};,]",string)
    m = re.findall(r"\".*\"",string)
    for i in r:
        if m:
            flag = 0
            for j in m:
                if i.group() in j:
                    flag = 1
            
            if flag==0:
                tup = (i.group(),'SPLSYM')
                tokens.append(tup)
         
        else:
            tup = (i.group(),'SPLSYM')
            tokens.append(tup)


def strings(string):
    r = re.finditer(r"\".*\"|\'.*\'",string)
    for i in r:
        tup = (i.group(),"STRING")
        tokens.append(tup)


def constants(string):
    r = re.finditer(r"\s*(\d+|\d*\.\d+)[,;\b]?",string)
    m = re.findall(r"\".*\"",string)
    for i in r:
        if m:
            flag = 0
            for j in m:
                if i.group(1) in j:
                    flag = 1
            
            if flag==0:
                tup = (i.group(1),"CONST")
                tokens.append(tup)

        else:
            tup = (i.group(1),"CONST")
            tokens.append(tup)

    
def removePPD(prog):
    ppd = []
    for i in prog:
        r = re.fullmatch(r"(#.*<.*>|#.*\s*\".*\")",i)
        if r:
            ppd.append(i)
            
    for i in ppd:
        prog.remove(i)
        
    return (prog)

