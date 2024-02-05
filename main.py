import requests
from tkinter import messagebox

url = 'https://api.roberty.app/prod/1/customer/robot/webhookCall'
payload = {
    "args": {
        "nome": "Aqui vai o nome do robô"
    },
    "token": "Aqui vai o token de Webhook gerado do robô"
}
response = requests.post(url, json=payload)

if response.status_code == 200:
    messagebox.showinfo('Sucesso', 'Roberty iniciado com sucesso!')
else:
    messagebox.showerror('Erro', f'Falha ao executar o Roberty. Código de status: {response.status_code}')