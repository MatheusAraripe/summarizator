import nltk
from googletrans import Translator


#traduzir do portugues pra ingles
def pt_to_en(texto):
    trans = Translator()
    
    text_en = ''
    for sent in nltk.sent_tokenize(texto):
        text_en += trans.translate(sent, dest = 'en').text
    return text_en

#traduzir do ingles para portugues
def en_to_pt(texto):
    trans = Translator()

    text_pt = trans.translate(texto, dest = 'pt').text
    return text_pt


#limpar a ultima sentenca do texto(sai incompleta)
def limpatexto(texto):
    text = ""
    for sent in nltk.sent_tokenize(texto).pop():
        text += sent
    return text
