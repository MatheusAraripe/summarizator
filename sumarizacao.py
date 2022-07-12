import heapq
import re
import string

import nltk
import spacy

#!python -m spacy download pt

nltk.download('punkt')

nltk.download("stopwords")


#Lematizaçao


#pln = spacy.load("pt_core_news_sm")

#Funcao que formata o texto. Retira stopwords, lematiza e passa tudo para minusculo

def format(txt):
  txt = re.sub (r'\s', ' ', txt)
  txt = txt.replace("\\n\\n", " ")
  txt = txt.lower()
  tokens = []
  vicios = ['né', 'Então', 'então', 'gente', 'Né']
  stopwords = nltk.corpus.stopwords.words("portuguese") + vicios
  for i in nltk.word_tokenize(txt):
    if i not in stopwords and i not in string.punctuation:
          tokens.append(i)
  texto_formatado = " ".join(elemento for elemento in tokens if not elemento.isdigit())
  return texto_formatado





#Funcao que retorna a porcentagem de sentencas que o usuario escolheu
def quantidade_de_sent(text, num):
  return round(num*(1/10)*text.count("."))




#Funcao que retorna uma lista das sentencas mais importantes baseada na frequencia de palavras, e uma lista de todas as sentencas 
def sumarizar_lemma(txt, quant_sentencas):
  txt = txt.replace("\\n\\n", " ")
  texto_format = format(txt)
  freq_palavras = nltk.FreqDist(nltk.word_tokenize(texto_format))
  freq_max  = max(freq_palavras.values())
  for palavra in freq_palavras:
    freq_palavras[palavra] = freq_palavras[palavra]/freq_max


  sentencas_txt = nltk.sent_tokenize(txt)

  nota_sentenca = {}
  for sentenca in sentencas_txt:
    for palavra in nltk.word_tokenize(sentenca):
      if palavra in freq_palavras.keys():
        if sentenca not in nota_sentenca:
          nota_sentenca[sentenca] = freq_palavras[palavra]
        else:
          nota_sentenca[sentenca] += freq_palavras[palavra]



  melhores_sentencas = heapq.nlargest(quant_sentencas, nota_sentenca, key = nota_sentenca.get)
  resumo = ""
  for sentenca in sentencas_txt:
    if sentenca in melhores_sentencas:
      resumo += sentenca
  return resumo, sentencas_txt, melhores_sentencas



