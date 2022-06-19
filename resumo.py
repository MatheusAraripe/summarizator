import openai

from API_SECRET import API_KEY

openai.api_key = API_KEY

#Usa a api do open AI para gerar um resumo do texto em ingles
def explicacao(texto):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Summarize this for a second-grade student:" + texto,
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    explicado = response["choices"]
    return explicado[0]["text"]

