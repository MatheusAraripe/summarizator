import glob
import os
import sys

import yaml
from yaml import dump, load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


def ajeitar(nome):
    nome = nome.split()
    nome.append(nome[0])
    nome.pop(0)
    nome = " ".join(nome)
    nome = nome.replace(",","")
    return nome


def busca_yaml(nome):
    nome = nome.lower()

    #varredura por todos os arquivos text
    for i in os.listdir("text/"):
        for fn in glob.glob(f"text/{i}"):
            with open(fn,"r") as f:
                content = f.read()
                # ignore the first line
                content = content[3:]
                p = content.find('---')
                header = content[0:p]
                d = yaml.load(header,Loader)
                d['text'] = content[p+4:]

                #busca por nomes correspondentes
                x = d['title'].lower()
                x = ajeitar(x)
                if nome == x:
                    return(d['text'].replace("«", "").replace("»",""))
    
    return "Sem correspondencia"

