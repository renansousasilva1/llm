import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("API_KEY")

# Criar cliente do chatbot
chat = ChatGroq(model='llama-3.3-70b-versatile', api_key=api_key)

print("Olá, bem-vindo! Eu serei seu Assistente-Virtual!")

API_URL = "http://xzeubl.conteige.cloud//CN/"  
   
resposta = requests.get(API_URL).content
print(resposta)

prompt = f"Eu quero que você use os dados que o user te mandou e reescreva tudo de forma adequada. Os dados enviados pelo usuário são notícias recebidas por uma API. Formate tudo de forma adequada e exporte um JSON com o texto estruturado com Título, Subtítulo e conteúdo reescrito de forma adequada e aprofundada. Estruture o JSON da seguinte forma: Título; Subtítulo; Conteúdo da notícia; Link para imagem da notícia (se disponível); Para isso você deve usar os dados enviados a seguir: '{resposta}'. Retorne somente o JSON estruturado. Apenas o conteúdo em JSON"


resposta2= chat.invoke(prompt)
print(resposta2.content)