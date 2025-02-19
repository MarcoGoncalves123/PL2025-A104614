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
    obras = []
    buffer = ""
    pattern = '^(.*);""?"?(.*);(\d*);([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});([^\n]+)$'
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
            obras.append(Obra(nome, desc, ano, periodo, compositor, duracao,id))
            buffer = ""
    return obras
            
        
read_line_by_line("TPC2\\obras.csv")

# ^(.*);"(.*)";(\d*);(\w*);(.*);(\d{2}:\d{2}:\d{2});