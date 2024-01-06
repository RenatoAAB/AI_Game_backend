import requests

# Replace these values with the actual values for your Carta model
carta_data = {
    'nome': 'Guerreiro fedido',
    'agilidade': 5,
    'ataque': 3,
    'vida' : 6,
    'custo' : 4

}

api_url = 'http://127.0.0.1:8000/create_carta'  # Peguei do urls.py o valor que defini para executar a view de postar uma carta nova, não pode ter a barra no final se
                                                # não está definido com a barra no final em urls.py -- da erro

response = requests.post(api_url, data=carta_data)

if response.status_code == 201:
    print("Entry added successfully.")
else:
    print("Failed to add entry. Status code:", response.status_code)
    print("Response content:", response.content.decode('utf-8'))