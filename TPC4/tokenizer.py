import re


def tokenizer(str):
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

    tok_regex = '|'.join([f'(?P<{id}>{expreg})' for (id,expreg) in token_specification])    
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex,str)
    for m in mo:
        dic = m.groupdict()

        if dic["SELECT"]:
            t = ("SELECT",dic['SELECT'],linha,m.span())
        elif dic["WHERE"]:
            t = ("WHERE",dic['WHERE'],linha,m.span())
        elif dic["LIMIT"]:
            t = ("LIMIT",dic['LIMIT'],linha,m.span())
        elif dic["VARIABLES"]:
            t = ("VARIABLES",dic['VARIABLES'],linha,m.span())
        elif dic["IDs"]:
            t = ("IDs",dic['IDs'],linha,m.span())
        elif dic["SEP"]:
            t = ("SEP",dic['SEP'],linha,m.span())
        elif dic["LPARENT"]:
            t = ("LPARENT",dic['LPARENT'],linha,m.span())
        elif dic["RPARENT"]:
            t = ("RPARENT",dic['RPARENT'],linha,m.span())
        elif dic["NUMBER"]:
            t = ("NUMBER",int(dic['NUMBER']),linha,m.span())
        elif dic["NEWLINE"]:
            linha += 1
        elif dic["SKIP"] or dic["COMMENT"]:
            pass 
        else:
            t = ("ERROR",dic['ERROR'],linha,m.span())
        
        if not dic['SKIP'] and not dic['NEWLINE'] and not dic['COMMENT']:
            reconhecidos.append(t)
    
    return reconhecidos


str = """ 
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000"""  

matches = tokenizer(str)
for match in matches:
    print(match)