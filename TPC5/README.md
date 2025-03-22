# PL2025-A104614

# Marco Soares Gonçalves

![Alt text](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/image.PNG)

# Máquina de Vending


**Objetivo**

Este tpc tem como objetivo construir um programa que simule uma máquina de vending.

# Resolução

Para resolver este problema comecei por criar um ficheiro [json_creator.py](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC5/json_creator.py) que tal como o nome indica, gera um ficheiro json que guarda o estado atual da máquina.
No que toca à máquina, decidi implementar todas as funcionalidades propostas com a adição ainda da opção **REABASTECER** (permite aumentar o stock de um produto já existente) e **ADICIONAR** (permite inserir novos produtos na máquina). 

 Estas são as funcionaliadades implementadas:
 
  - LISTAR
  - MOEDA
  - SELECIONAR
  - REABASTECER
  - ADICIONAR 
  - SAIR

Junto com estas funcionalidades foi também necessária a implementação de uma lógica de saldo. Para tal criei uma função que me devolve o saldo disponível em euros e em cêntimos, para que depois estes possam ser apresentados no formato XeYc ao utilizador ,onde
"e" representa os euros e "c" os cêntimos. Esta função foi necesária pois ao longo do programa decidi trabalhar com o saldo em cêntimos.

Para além disso foi criada uma função "guardar_estado" que apenas é chamada quando a opção "SAIR" é selecionada. Esta função é a que guarda o estado da máquina no ficheiro  [stock.json](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC5/stock.json)

# Exemplo de utilização

```
maq: 22/03/2025, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR 
maq:
cod   nome                      quant      preco  
--------------------------------------------------
A23   água 0.5L                 10         0.70   
B12   sumo laranja 1L           5          1.50   
C34   coca-cola 1.5L            12         1.80   
D56   pão de forma              6          1.20   
E78   leite 1L                  10         0.90   
F90   manteiga 250g             4          2.30   
G11   queijo flamengo 200g      7          2.70   
H22   fiambre peru 150g         9          2.10   
I33   café solúvel 200g         3          3.50   
J44   açúcar 1kg                11         1.00   
K55   arroz 1kg                 8          1.30   
L66   massa esparguete 500g     15         0.90   
M77   óleo girassol 1L          5          2.50   
N88   sal fino 1kg              14         0.60   
O99   chocolate negro 100g      6          1.80   
A450  TESTE                     5          1.50   
>> MOEDA 1e, 50c   
maq: Saldo = 1e5c
>> SELECIONAR A23  
>> REABASTECER A23
Quantidade a reabastecer: 5
>> ADICIONAR       
Introduza o código do produto: m45
Introduza o nome do produto: TESTE2
Introduza a quantidade do produto em stock: 5
Introduza o preço do produto: 1.5
Produto adicionado com sucesso
>> LISTAR
maq:
cod   nome                      quant      preco  
--------------------------------------------------
A23   água 0.5L                 14         0.70   
B12   sumo laranja 1L           5          1.50   
C34   coca-cola 1.5L            12         1.80   
D56   pão de forma              6          1.20   
E78   leite 1L                  10         0.90   
F90   manteiga 250g             4          2.30   
G11   queijo flamengo 200g      7          2.70   
H22   fiambre peru 150g         9          2.10   
I33   café solúvel 200g         3          3.50   
J44   açúcar 1kg                11         1.00   
K55   arroz 1kg                 8          1.30   
L66   massa esparguete 500g     15         0.90   
M77   óleo girassol 1L          5          2.50   
N88   sal fino 1kg              14         0.60   
O99   chocolate negro 100g      6          1.80   
A450  TESTE                     5          1.50   
m45   TESTE2                    5          1.50   
>> SAIR
maq: Pode retirar o troco:0x2e 0x1e 1x20c 1x10c 1x5c 
maq: Até à próxima.
````

# Link
[Source Code](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC5/vending_machine.py)
