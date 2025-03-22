# PL2025-A104614

# Marco Soares Gonçalves

![Alt text](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/image.PNG)

# Recursivo Descendente para expressões aritméticas


# Objetivo

Este tpc tem como objetivo criar um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor de frases deste género: 

```
2+3
67-(2+3*4)
(9-2)*(13-4)
````

# Resolução

Para implementar a solução comecei por definir a gramática do problema no ficheiro [maquete.txt](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC6/maquete.txt). Tendo isto em mente esta foi a 
gramática concreta final (inspirada na aula T da semana 6) que planeei: 

```
  Exp -> Termo Exp2 
  Exp2 -> "+" Exp
      |   "-" Exp
      |   Epsilon
  
  Termo -> Fator Termo2
  Termo2 -> "*" Termo
          | Epsilon
  
  Fator -> "(" Exp ")" | num 
```

De seguida criei o ficheiro [recursivo_descendente.py](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC6/recursivo_descendente.py) no qual comecei por criar um tokenizer que conseguisse reconhecer todos os tokens
necessários para o funcionamento da linguagem. Para isto usufruí da biblioteca "ply.lex". 

De seguida "converti" a minha gramática concreta final em 5 parsers diferentes, parsers estes que me permitem reconhecer as expressões aritméticas e calcular os seus respetivos valores :

 - parse_exp
 - parse_exp2
 - parse_termo
 - parse_termo2
 - parse_fator

# Resultados

Para a linguagem descrita no enunciado obtemos os seguintes resultados:

```
5
53
63
```

