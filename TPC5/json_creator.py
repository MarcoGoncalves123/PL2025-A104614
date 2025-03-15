import json


def create_json(stock):
    
    with open("stock.json", 'w',encoding='utf-8') as file:
        json.dump(stock,file,indent=4,ensure_ascii=False)
        


stock = [
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7},
    {"cod": "B12", "nome": "sumo laranja 1L", "quant": 5, "preco": 1.5},
    {"cod": "C34", "nome": "coca-cola 1.5L", "quant": 12, "preco": 1.8},
    {"cod": "D56", "nome": "pão de forma", "quant": 6, "preco": 1.2},
    {"cod": "E78", "nome": "leite 1L", "quant": 10, "preco": 0.9},
    {"cod": "F90", "nome": "manteiga 250g", "quant": 4, "preco": 2.3},
    {"cod": "G11", "nome": "queijo flamengo 200g", "quant": 7, "preco": 2.7},
    {"cod": "H22", "nome": "fiambre peru 150g", "quant": 9, "preco": 2.1},
    {"cod": "I33", "nome": "café solúvel 200g", "quant": 3, "preco": 3.5},
    {"cod": "J44", "nome": "açúcar 1kg", "quant": 11, "preco": 1.0},
    {"cod": "K55", "nome": "arroz 1kg", "quant": 8, "preco": 1.3},
    {"cod": "L66", "nome": "massa esparguete 500g", "quant": 15, "preco": 0.9},
    {"cod": "M77", "nome": "óleo girassol 1L", "quant": 5, "preco": 2.5},
    {"cod": "N88", "nome": "sal fino 1kg", "quant": 14, "preco": 0.6},
    {"cod": "O99", "nome": "chocolate negro 100g", "quant": 6, "preco": 1.8},
]

create_json(stock)