# PL2025-A104614

# Marco Soares Gonçalves

![Alt text](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/image.PNG)

# Conversor de MarkDown para HTML

### **Objetivo**

Nesta semana o objetivo do TPC é criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic
Syntax" da Cheat Sheet

Para isso é necessário tratar os seguintes casos: 

- **Cabeçalhos:** linhas iniciadas por "# texto", ou "## texto" ou "### texto"
  
- **Bold:** pedaços de texto entre "**"
  
- **Itálico:** pedaços de texto entre "*"
  
- **Lista numerada:**
   - **1.** Primeiro item
   - **2.** Segundo item
   - **3.** Terceiro item
      
- **Link:** [texto](endereço URL)
  
- **Imagem:** ![texto alternativo](path para a imagem)


### **Resolução** 

Para resolver este problema decidi utilizar 8 expressões regulares diferentes, uma para cada caso previamente listado:
``` Python
    pattern_for_headers_h1 = r"^#\s+(.*)$"  
    pattern_for_headers_h2 = r"^##\s+(.*)$"  
    pattern_for_headers_h3 = r"^###\s+(.*)$"  
    pattern_for_bolds = r"\*\*([^*]+)\*\*" 
    pattern_for_italic = r"\*([^*]+)\*"  
    pattern_for_image = r"!\[(.*)\]\((.*)\)"
    pattern_for_link = r"\[(.*)\]\((.*)\)"
    pattern_for_list = r"(\d+\.)\s(.*)"
```

A resolução começa portanto com a leitura do ficheiro [teste.md](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC3/teste.md), sendo que este é o ficheiro que pretendemos converter.

De seguida é utilizado o comando ```re.sub ``` para substituir no contéudo lido todos os **Cabeçalhos**. Após a substituição dos cabeçalhos é feita a substituição dos **Negritos** e e **Itálicos**, respetivamente. Esta ordem **TEM**
de ser respeitada pois a expressão regular para encontrar os Itálicos iria dar match com os  "*"  interiores dos Negritos e consequentemente invalidá-los.

Tendo isto feito, passamos à substituição das **Imagens** e **Links**, respetivamente. Mais uma vez, a ordem aqui é crucial pois detetar primeiro os Links utilizando a expressão regular definida irá invalidar a expressão que deteta as Imagens. 

Para terminar é feito o processo de substituição das **Listas** , que é considerávelmente mais complexo do que os outros e ocorre em conjunto com a escrita no ficheiro [results.txt](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC3/results.txt) . Primeiro, o contéudo html que já contém as alterações de todos os outros campos 
dividido em linhas. Após isso, para cada linha é tentado um match com a expressão regular que deteta o padrão de listas. Caso o match aconteça é escrito para o ficheiro e seja detetado que estamos no incío da lista , então será escrito para o ficheiro
a linha ```"<ol>\n"```  de modo a simbolizar o início da lista. Em seguida, enquanto a lista ainda não tiver terminado, todas as linhas são formatadas para seguirem o seguinte padrão ```<li>{match.group(2)}</li>\n```. Caso seja detetado o fim da lista 
então a linha ```"</ol>\n"``` é escrita no ficheiro. No caso de não haver match a linha atual é simplsmente escrita no ficheiro.


### **Resultados**

Olhando para o ficheiro [results.txt](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC3/results.txt) conseguimos perceber que os resultados são extamente aqueles descritos no enunciado.

### **Referências**

**Link** : [Source Code](https://github.com/MarcoGoncalves123/PL2025-A104614/blob/main/TPC3/conversor.py)
    
