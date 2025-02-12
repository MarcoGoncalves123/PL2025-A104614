import sys 

def On_Off(linha):
    i = 0
    res = 0
    on = True
    acc = ''
    while i < len(linha):
        if (linha[i] in "1234567890" and on):
            acc += linha[i]
        elif acc and on:
            res += int(acc)
            acc = '' 
                        
        if(linha[i] == '='):
            print(res) 
            
        if linha[i].lower() == "o":
            if(linha[i+1].lower() == "n"):
                on = True
            elif(linha[i+1].lower() == "f"):
                if(linha[i+2].lower() == "f"):
                    on = False
        i+=1
    
On_Off("12abc34=On56xyz789=OFF987=Onabc123=")
