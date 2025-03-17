import json
import re
from datetime import datetime


def carregar_estado(path):
    with open (path,"r",encoding="utf-8") as file:
        stock = json.load(file)
        data = datetime.today().strftime("%d/%m/%Y")
        stock_dict = {product["cod"] : product for product in stock}
        print(f'maq: {data}, Stock carregado, Estado atualizado.')
        return stock_dict
        
def listar_stock(stock):
    print("maq:")
    print(f"{'cod':<5} {'nome':<25} {'quant':<10} {'preco':<7}") 
    print("-" * 50)  
    
    for product in stock.values():
        print(f"{product['cod']:<5} {product['nome']:<25} {product['quant']:<10} {product['preco']:<7.2f}")

def inserir_moeda(pedido):
    pattern = r'2e|1e|50c|20c|10c|5c'  
    matches = re.findall(pattern, pedido)  
    saldo = 0
    if matches:
        for match in matches:
            if match[1] == "e":
                saldo += (int(match[0]) * 100)
            else:
                saldo += int(int(match[0]))
    else:
        print("Não reconheci nenhuma moeda.")
    return saldo

def saldo_em_euros(saldo):
    numero = saldo / 100
    euros = int(numero)  
    centimos = round((numero - euros) * 100)
    return euros, centimos

def select_product(cod,saldo,stock):
    if cod not in stock:
        print("O cod inserido não corresponde a nenhum produto")
        return saldo

    product = stock.get(cod)
    
    if product["quant"] == 0:
        print("maq: Não existe produto em stock")   
        return saldo
        
    if (product["preco"] * 100) > saldo:
        print("maq: Saldo insufuciente para satisfazer o seu pedido")   
        euros,centimos = saldo_em_euros(saldo)
        euros_p,centimos_p = saldo_em_euros(product["preco"] * 100)
        str = f'maq: Saldo ='
        if euros > 0:
            str += (f" {euros}e")
            
        str += f' {centimos}c; Pedido:'
        
        if euros_p > 0:
            str += (f" {euros_p}e")
        str += f' {centimos_p}c;'
        print(str)
        return saldo
        
    saldo -= product["preco"] * 100 
    product["quant"] -= 1        

    return saldo
    
def reabastecer(cod,stock):
    if cod not in stock:
        print("O cod inserido não corresponde a nenhum produto")
        return 

    product = stock.get(cod)  
    valor = input("Quantidade a reabastecer: ")
    if valor.isdigit():
        product["quant"] += int(valor)
    else:
        print("O valor introduzido não é um dígito")
 
def adicionar(stock):
    cod = input("Introduza o código do produto: ")
    
    if cod in stock:
        print("Esse código já pertence a um produto: ")
        return
            
    nome = input("Introduza o nome do produto: ")
    
    quantidade = input("Introduza a quantidade do produto em stock: ")
    if not quantidade.isdigit():
        print("A quantidade introduzida é inválida")
        return
    
    preco = input("Introduza o preço do produto: ")
    try:
        preco = float(preco) 
    except ValueError:
        print("O preço introduzido é inválido.")
        return

    novo_produto = {
        "cod": cod,
        "nome": nome,
        "quant": int(quantidade),  
        "preco": float(preco)
    }
    
    stock[cod] = novo_produto
    print("Produto adicionado com sucesso")    
       
def devolve_troco(saldo):
    euros,centimos = saldo_em_euros(saldo)
    
    cinquenta_c = 0
    vinte_c = 0
    dez_c = 0
    cinco_c = 0
    um_e = 0
    dois_e = 0

    while centimos != 0:
        while centimos >= 50:
            cinquenta_c += 1
            centimos -= 50
        
        while centimos >= 20:
            vinte_c += 1
            centimos -= 20
            
        while centimos >= 10:
            dez_c += 1
            centimos -= 10
    
        while centimos >= 5:
            cinco_c += 1
            centimos -= 5
            
        while centimos >= 5:
            cinco_c += 1
            centimos -= 5
                    
    str = "maq: Pode retirar o troco:"
    
    while euros >= 2:
        dois_e += 1
        euros -= 2
    
    str += (f"{dois_e}x2e ")

    while euros >= 1:
        um_e += 1
        euros -= 1
        
    str += (f"{um_e}x1e ")
    
    if cinquenta_c > 0:
        str += (f"{cinquenta_c}x50c ")
    if vinte_c > 0:
        str += (f"{vinte_c}x20c ")
    if dez_c > 0:
        str += (f"{dez_c}x10c ")
    if cinco_c > 0:
        str += (f"{cinco_c}x5c ")
    
    print(str)
    print("maq: Até à próxima.")
    
def guardar_estado(path, stock):
    with open(path, "w", encoding="utf-8") as file:
        stock_list = list(stock.values()) 
        json.dump(stock_list, file, ensure_ascii=False, indent=4)  
    

def atendimento(stock):
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    saldo = 0
    running = True
    while running:
        pedido = input(">> ")
        if pedido == "LISTAR":
            listar_stock(stock)
        if re.match(r'MOEDA',pedido):
            saldo += inserir_moeda(pedido) 
            euros,centimos = saldo_em_euros(saldo)
            if euros > 0:
                print(f'maq: Saldo = {euros}e{centimos}c')  
            else:
                print(f'maq: Saldo = {centimos}c')  
        if match := re.match(r'(SELECIONAR) (.*)',pedido):
            saldo = select_product(match.group(2),saldo,stock)
        if match := re.match(r'(REABASTECER) (.*)',pedido):
            reabastecer(match.group(2),stock)
        if match := re.match(r'(ADICIONAR)',pedido):
            adicionar(stock)
        if pedido == "SAIR":
            running = False
            guardar_estado("stock.json",stock)
            if saldo > 0:
                devolve_troco(saldo)
                
    
def main():
    stock = carregar_estado("stock.json")
    atendimento(stock)


if __name__ == "__main__":
    main()