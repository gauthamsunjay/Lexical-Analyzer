import re
'''
functions for the tokens

'''
keywords = ['auto','break','case','char','double','else','enum','extern','int','long','register','return','struct','switch','typedef','union','const','continue','default','do','float','for','goto','if','short','signed','sizeof','static','unsigned','void','volatile','while']

tokens = []

def operator(string):
    r = re.finditer(r"[\+\*=/\-%]",string)
    for i in r:
        tup = (i.group(),'OP')
        tokens.append(tup)

def identifiers(string):
    r = re.finditer(r"\w+",string)
    for i in r:
        if(i.group() in keywords):
            tup = (i.group(),'KEYWORD')
            tokens.append(tup)
        
        else:
            tup = (i.group(),'ID')
            tokens.append(tup)

def spSymbols(string):
    r = re.finditer(r"[\(\)\{\};,]",string)
    for i in r:
        tup = (i.group(),'SPLSYM')
        tokens.append(tup)

def strings(string):
    r = re.finditer(r"\".*\"",string)
    for i in r:
        tup = (i.group(),"STRING")
        tokens.append(tup)

def constants(string):
    r = re.finditer(r"=\s+(.*);",string)
    for i in r:
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

