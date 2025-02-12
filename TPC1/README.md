# PL2025-A104614

# Marco Soares Gonçalves

![Alt text](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/image.PNG)

# Somador on/off

**Objetivo**

Este programa tem como objetivo somar todas as sequências de digitos que encontre num texto, respeitando um mecanismo de ativação/desativação:
- Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
- Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
- Sempre que o encontrar o caractér "=", o resultado da soma é colocado na saída.

**Resolução** 

Para implementar a solução utilizei:
- Um ciclo "while" que permite processar cada caracter individualmente;
- Uma flag "on" que identifica se a soma está ou não ativa;
- Um buffer temporário (acc) que armazena os dígitos de um número à medida que estes são encontrados. Assim que se encontre um caracter que não é um dígito, o buffer é convertido para um inteiro e somado ao acumulador (res);
- Um acumulador (res) que armazena a soma das sequências de dígitos caso a flag "on" esteja ativa;

Links:
[Source Code](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC1/Tpc1.py)
[Resultados]()
    

