# PL2025-A104614

# Marco Soares Gonçalves

![Alt text](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/image.PNG)

# Analisador Léxico
### **Objetivo**
Neste TPC foi nos proposto "Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género":

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
 ?s a dbo:MusicalArtist.
 ?s foaf:name "Chuck Berry"@en .
 ?w dbo:artist ?s.
 ?w foaf:name ?nome.
 ?w dbo:abstract ?desc
} LIMIT 1000
```

### **Resolução** 

A resolução deste problema começou pela identificação de cada token presente na string mencionada. Para isso decidi criar uma lista **token_specification** que contém as ex+ressões regulares para todos os 
tokens considerados.

```
    token_specification = [
        ('COMMENT',r'#.*'),
        ('SELECT',r'select'),
        ('WHERE',r'where'),
        ('LIMIT',r'LIMIT'),
        ('VARIABLES',r'\?[a-zA-z]+'),
        ('IDs',r'[a-zA-z]+:\s*[a-zA-Z"@\s]*'),
        ('SEP',r'\.'),
        ('LPARENT',r'{'),
        ('RPARENT',r'}'),
        ('NUMBER',r'\d+'),
        ('NEWLINE',r'\n'),
        ('SKIP',r'[\s\t]+'),
        ('ERROR',r'.')
    ]
```

### **Resultados**

``` 
('SELECT', 'select', 2, (34, 40))
('VARIABLES', '?nome', 2, (41, 46))
('VARIABLES', '?desc', 2, (47, 52))
('WHERE', 'where', 2, (53, 58))
('LPARENT', '{', 2, (59, 60))
('VARIABLES', '?s', 3, (61, 63))
('ERROR', 'a', 3, (64, 65))
('IDs', 'dbo:MusicalArtist', 3, (66, 83))
('SEP', '.', 3, (83, 84))
('VARIABLES', '?s', 4, (85, 87))
('IDs', 'foaf:name "Chuck Berry"@en ', 4, (88, 115))
('SEP', '.', 4, (115, 116))
('VARIABLES', '?w', 5, (117, 119))
('IDs', 'dbo:artist ', 5, (120, 131))
('VARIABLES', '?s', 5, (131, 133))
('SEP', '.', 5, (133, 134))
('VARIABLES', '?w', 6, (135, 137))
('IDs', 'foaf:name ', 6, (138, 148))
('VARIABLES', '?nome', 6, (148, 153))
('SEP', '.', 6, (153, 154))
('VARIABLES', '?w', 7, (155, 157))
('IDs', 'dbo:abstract ', 7, (158, 171))
('VARIABLES', '?desc', 7, (171, 176))
('RPARENT', '}', 8, (177, 178))
('LIMIT', 'LIMIT', 8, (179, 184))
('NUMBER', 1000, 8, (185, 189))

``` 

### **Referências**

**Link** : [Source Code](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC4/tokenizer.py)
    
