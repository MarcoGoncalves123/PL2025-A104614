import re


class Obra:
    def __init__(self, nome, descricao, anoCriacao, periodo, compositor, duracao, _id):
        self.nome = nome
        self.descricao = descricao
        self.anoCriacao = anoCriacao
        self.periodo = periodo
        self.compositor = compositor
        self.duracao = duracao
        self._id = _id

    def __str__(self):
        return f"Obra({self.nome}, {self.anoCriacao}, {self.periodo}, {self.compositor}, {self.duracao}, {self._id})"   
        

def read_line_by_line(path):
    compositores = []
    obras_por_periodo = {}
    obras_por_periodo_e_titulo = {}
    buffer = ""
    pattern = '^([^;]+);"?((?:[^"]|"{0,2})*)"?;(\d*);([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});([^\n]+)$'
    f = open(path,'r',encoding='utf-8')
    next(f)
    for linha in f.readlines():
        linha_clean = linha.strip("\n") 
        buffer += linha_clean                
        match = re.match(pattern,buffer)
        if match:
            nome = match.group(1)
            desc = match.group(2)
            ano = match.group(3)
            periodo = match.group(4)
            compositor = match.group(5)
            duracao = match.group(6)
            id = match.group(7)
            obra = Obra(nome, desc, ano, periodo, compositor, duracao,id)
            
            compositores.append(compositor)
            
            if obras_por_periodo.get(periodo) is None:
                obras_por_periodo[periodo] = [obra]
            else:
                obras_por_periodo[periodo].append(obra)
        
            if obras_por_periodo_e_titulo.get(periodo) is None:
                obras_por_periodo_e_titulo[periodo] = [nome]
            else:
                obras_por_periodo_e_titulo[periodo].append(nome)
            
            buffer = ""
    return obras_por_periodo_e_titulo,compositores,obras_por_periodo
            
    
def main():
    obras_por_periodo_e_titulo,compositores,obras_por_periodo = read_line_by_line("obras.csv")
    
    # Query 1
    compositores.sort()
    print()
    print("-----------------------------------Lista ordenada dos compositores musicais-----------------------------------")
    for compositor in compositores:
        print(compositor)
    
    
        
    # Query 2
    print()
    print("-----------------------------------Quantas obras por período-----------------------------------")
    for periodo,lista in obras_por_periodo.items():
        print(f'Período: {periodo} | Quantidade: {(len(lista))}')
    
            
    # Query 3
    print()
    print("-----------------------------------Dicionário de obras por período-----------------------------------")
    for periodo,lista in obras_por_periodo_e_titulo.items():
        lista.sort()
        print("-------------------------------")
        print(f'Período: {periodo}')
        print(" ")
        print("obras:")
        for item in lista:
            print(" " + item)
        
if __name__ == "__main__":
    main()
