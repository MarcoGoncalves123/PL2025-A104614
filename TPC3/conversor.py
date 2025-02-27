import re


def conversor(path):
    pattern_for_headers_h1 = r"^#\s+(.*)$"  
    pattern_for_headers_h2 = r"^##\s+(.*)$"  
    pattern_for_headers_h3 = r"^###\s+(.*)$"  
    pattern_for_bolds = r"\*\*([^*]+)\*\*" 
    pattern_for_italic = r"\*([^*]+)\*"  
    pattern_for_image = r"!\[(.*)\]\((.*)\)"
    pattern_for_link = r"\[(.*)\]\((.*)\)"

    
    pattern_for_list = r"(\d+\.)\s(.*)"  

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Substituir headers
    html_content = re.sub(pattern_for_headers_h1, r'<h1>\1</h1>', content, flags=re.MULTILINE)
    html_content = re.sub(pattern_for_headers_h2, r'<h2>\1</h2>', html_content,flags=re.MULTILINE)
    html_content = re.sub(pattern_for_headers_h3, r'<h3>\1</h3>', html_content,flags=re.MULTILINE)

    # Bold vem primeiro que os itálicos para retira todas as possibilidades em que "**" aparece, tornando
    # assim mais fácil a deteção de "*"
    html_content = re.sub(pattern_for_bolds, r'<b>\1</b>', html_content)
    html_content = re.sub(pattern_for_italic, r'<i>\1</i>', html_content)
    
    # Imagem vem primeiro para nos livrarmos de todos os casos em que ! aparece antes dos [] 
    # garantindo que nenhuma imagem é confundida com um URL
    
    html_content = re.sub(pattern_for_image,r'<img src="\2" alt="\1"/>', html_content,flags=re.MULTILINE)
    html_content = re.sub(pattern_for_link,r'<a href="\2">\1</a>', html_content,flags=re.MULTILINE)
    
    #Listas deixo para o final
    inside_list = False
    
    with open("results.txt", 'w', encoding='utf-8') as result:
        lines = html_content.split("\n")
        for line in lines:
            match = re.match(pattern_for_list,line)
            if match:
                if inside_list is False:
                    inside_list = True
                    result.write("<ol>\n")   
                result.write(f"<li>{match.group(2)}</li>\n")
            else:
                if inside_list:
                    inside_list = False
                    result.write("</ol>\n")
                result.write(line + "\n")
            
    print(html_content)

conversor("teste.md")
