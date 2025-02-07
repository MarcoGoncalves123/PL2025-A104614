import sys 

def On_Off(linha):
    i = 0
    res = 0
    on = True
    while i < len(linha):
        if(linha[i] == "="):
            print(res)
            i += 1 
        elif linha[i] in "1234567890" and on:
            res += int(linha[i])
            i += 1
        elif linha[i].lower() == "o":
            i += 1
            if(linha[i].lower() == "n"):
                i += 1
                on = True
            elif(linha[i].lower() == "f"):
                i += 1
                if(linha[i].lower() == "f"):
                    on = False
                    i += 1
        else:
            i += 1
    
On_Off("12abc34=On56xyz789=OFF987=On0abc123=")
