
from flask import Flask, render_template, request

import sumarizacao as sm

#from resumo import *
#from tradutor import *


sentencas = []
melhores_sentencas = []



app = Flask(__name__)


#Rota da pagina inicial
@app.route("/")
def index():
    return render_template("index.html")


#Rota da pagina corespondente a entrada de textos do usuario
@app.route("/input", methods = ['GET', 'POST'])
def input():
    return render_template("input.html")




#Rota auxiliar para realizar as operecoes no texto de entrada do usuario
@app.route("/analise", methods = ["GET","POST"])
def analise():
    global sentencas
    global melhores_sentencas

    data = request.json['user_input']
    quant = int(request.json['quant'])

    quantidade = sm.quantidade_de_sent(data,quant)


    resumo,sentencas,melhores_sentencas = sm.sumarizar(data, quantidade)




    return resumo



#Rota auxiliar para realizar as operecoes nos arquivos de texto de entrada do usuario
@app.route("/file", methods = ["GET","POST"])
def f():
    global sentencas
    global melhores_sentencas

    data = request.json['user_input']
    quant = int(request.json['quant'])


    quant = sm.quantidade_de_sent(data,quant)

    resumo, sentencas, melhores_sentencas = sm.sumarizar(data, quant)

    #text_en = pt_to_en(resumo)

    #summ_text_en = explicacao(data)

    #summ_text_pt = en_to_pt(summ_text_en)
    

    return resumo

   

#Rota da pagina onde e exibido o texto completo
@app.route("/textos")
def textos():
    return render_template("textos.html", sentencas = sentencas, melhores_sentencas = melhores_sentencas)


