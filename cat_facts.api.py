#TESTE REQUESTS
#Chamar a biblioteca do cliente http
import requests

#Preciso criar uma variável para armazenar url base, o endpoint (caminho) e a resposta da requisição

url_base = 'https://catfact.ninja/'
endpoint = f'{url_base}/fact'

# while True:
response = requests.get(endpoint)

#Print do código de status http
# print(response.status_code)
# print (response.text)

#Crio uma variável para chamar o json. Ele pega o json da resposta e converte para dicionário

cat_facts = response.json()
print ('Haha criei minha primeira FART CATS: ', cat_facts['fact'])
# print()
