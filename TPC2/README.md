# PL2025-A104614

# Marco Soares Gonçalves

![Alt text](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/image.PNG)

# Análise de um dataset de obras musicais

**Objetivo**

Este programa tem como objetivo fazer parsing de um ficheiro **.csv** que contém informações sobre diversas obras musicais, e com isso criar as seguintes queries:
- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.

**Resolução** 

A solução foi estruturada em torno da leitura do arquivo [obras.csv](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC2/obras.csv) e a criação de objetos que representam as diversas obras musicais.
Para isso utilizei um ciclo de leitura linha a linha, no qual cada uma destas é adicionada a um buffer. Em seguida verifica-se se a expressão regular definida dá match com o conteudo do buffer. Quando este match ocorre,
as informações relevantes são armazenadas nas 3 seguintes estruturas:

- Lista de compositores: Armazena o nome de cada compositor, para mais tarde gerar a query 1 (lista ordenada de compositores).
- Dicionário de obras por período: Armazena para cada período todas as obras escritas no mesmo, para mais tarde gerar a query 2 (quantidade de obras por período).
- Dicionário de obras por período e título: Armazena para cada período o nome de cada obra escrita no mesmo, para mais tarde gerar a query 3 (lista alfabética de títulos das obras por período).

**Expressão regular**

A validação de cada obra do arquivo .csv é feita através de uma expressão regular, que garante que os dados estejam no formato esperado:
- Nome da obra
- Descrição da obra
- Ano de criação
- Período histórico
- Compositor
- Duração
- ID da obra

Tendo isto em mente esta foi a regex definida:

```python
     pattern = '^([^;]+);"?((?:[^"]|"{0,2})*)"?;(\d*);([^;]+);([^;]+);(\d{2}:\d{2}:\d{2});([^\n]+)$'
````


Captura o nome da obra, que pode ser composto por qualquer caracter exceto ";"
```python
^([^;]+);
````

Captura a descrição da obra, que pode ser composta por qualquer caracter e pode conter citações ("""Zärtliche Liebe"").
```python
"?((?:[^"]|"{0,2})*)"?;
````

Captura o ano de criação que é apenas composto por dígitos
```python
(\d*)
```

Captura o período em que foi criada a obra. Visto que em certos casos o periodo possui acentos ("Clássico") decidi não utilizar o "\w" para detetar este campo. Para resolver esse problema
procuro por qualquer sequência de caracteres que não sejam ";" 
```python
([^;]+)
````

Captura o compositor de forma semelhante ao campo anterior
```python
([^;]+)
```

Captura a duração da obra que deve seguir o seguinte formato : (DD-DD-DD) onde D representa um **Dígito**
```python
(\d{2}:\d{2}:\d{2})
```

Finalmente é capturado o id da obra, que pode ser qualquer sequência de caracteres até ao final da linha
```python
([^\n]+)$'
```

**Resultados**

Após o parsing dos dados são executadas e impressas no ecrã as 3 queries:

- A lista de compositores ordenada alfabeticamente
  - Alessandro Stradella
  - Antonio Maria Abbatini
  - Bach, Johann Christoph
  - Bach, Johann Michael
  - Bach, Johann Michael
  - Bach, Wilhelm Friedemann
  - Bach, Wilhelm Friedemann
  - Bach, Wilhelm Friedemann
  - Balbastre, Claude
  - Balbastre, Claude
  - Baldassare Galuppi
  - Barbara of Portugal
  - Barbara of Portugal
  - Benda, Franz
  - Benda, Franz
  - Benda, Franz
  - Bernardo Pasquini
  - Biber, Heinrich Ignaz Franz
  - Bononcini, Giovanni Battista
  - Boyvin, Jacques
  - Bull, John
  - Cabanilles, Juan Bautista
  - Cabanilles, Juan Bautista
  - Caldara, Antonio
  - etc ... 
  
- A distribuição das obras por período
  - Período: Barroco | Quantidade: 26
  - Período: Clássico | Quantidade: 15
  - Período: Medieval | Quantidade: 48
  - Período: Renascimento | Quantidade: 41
  - Período: Século XX | Quantidade: 18
  - Período: Romântico | Quantidade: 19
  - Período: Contemporâneo | Quantidade: 7 

- As obras organizadas por período:
  - Período: Barroco

  - obras:
    - Ab Irato
    - Die Ideale, S.106
    - Fantasy No. 2
    - Hungarian Rhapsody No. 16
    - Hungarian Rhapsody No. 5
    - Hungarian Rhapsody No. 8
    - Impromptu Op.51
    - In the Steppes of Central Asia
    - Mazurkas, Op. 50
    - Military Band No. 1
    - Nocturne in C minor
    - Paganini Variations, Book I
    - Polonaise Op. 44
    - Polonaise-Fantasie
    - Polonaises Op.71
    - Preludes Op. 11
    - Preludes Op. 49
    - Prince Rostislav
    - Rage Over a Lost Penny
    - Rondo Op. 5
    - Shéhérazade, ouverture de féerie
    - Symphonies de Beethoven
    - The Rondo
    - Transcendental Études
    - Études Op. 25
    - Études Op.10
  - Etc ...


**Link** : [Source Code](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC2/analise_obras.py)
    
