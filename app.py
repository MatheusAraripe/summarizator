from flask import Flask, render_template, request

import sumarizacao as sm
from find import *
from resumo import *
from tradutor import *

sentencas = []
melhores_sentencas = []
file_txt = "" 


app = Flask(__name__)


#Rota da pagina inicial
@app.route("/")
def index():
    return render_template("index.html")


#Rota da pagina corespondente a entrada de textos do usuario
@app.route("/input", methods = ['GET', 'POST'])
def input():
    return render_template("input.html")


#Rota da pagina do CPDOC
@app.route("/cpdoc", methods = ['GET', 'POST'])
def cpdoc():
    return render_template("cpdoc.html")


#Rota auxiliar para realizar as operacoes nos textos do cpdoc
@app.route("/textcpdoc", methods = ["GET","POST"])
def textcpdoc():
    data = request.json['user_input']
    text = busca_yaml(data)


    global sentencas
    global melhores_sentencas

    quant = int(request.json['quant'])

    sentencas, melhores_sentencas = sm.sumarizar_lemma(text, quant)

    text_en = pt_to_en(text)

    summ_text_en = explicacao(text_en)

    summ_text_pt = en_to_pt(summ_text_en)
    summ_text_pt = limpatexto(summ_text_pt)

    return summ_text_pt



#Rota auxiliar para realizar as operecoes no texto de entrada do usuario
@app.route("/analise", methods = ["GET","POST"])
def analise():
    global sentencas
    global melhores_sentencas

    data = request.json['user_input']
    quant = int(request.json['quant'])


    sentencas, melhores_sentencas = sm.sumarizar_lemma(data, quant)

    text_en = pt_to_en(data)

    summ_text_en = explicacao(text_en)

    summ_text_pt = en_to_pt(summ_text_en)
    summ_text_pt = limpatexto(summ_text_pt)

    return summ_text_pt



#Rota auxiliar para realizar as operecoes nos arquivos de texto de entrada do usuario
@app.route("/file", methods = ["GET","POST"])
def f():
    global sentencas
    global melhores_sentencas

    data = request.json['user_input']
    quant = int(request.json['quant'])


    sentencas, melhores_sentencas = sm.sumarizar_lemma(data, quant)

    text_en = pt_to_en(data)

    summ_text_en = explicacao(text_en)

    summ_text_pt = en_to_pt(summ_text_en)
    

    return summ_text_pt

   



#Rota da pagina onde e exibido o texto completo
@app.route("/textos")
def textos():
    return render_template("textos.html", sentencas = sentencas, melhores_sentencas = melhores_sentencas)



app.run(debug= True)
