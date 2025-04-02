import requests

def converter_moeda(valor, moeda_origem, moeda_destino):
    """
    Converte um valor entre moedas usando a API ExchangeRate-API
    
    Parâmetros:
    valor (float): Valor a ser convertido
    moeda_origem (str): Código da moeda de origem (ex: 'BRL')
    moeda_destino (str): Código da moeda de destino (ex: 'USD')
    
    Retorna:
    float: Valor convertido
    """
    try:
        # Chave de API - você precisará obter uma gratuitamente em https://www.exchangerate-api.com/
        API_KEY = '3b5412e0510be406e8010451'
        url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{moeda_origem}/{moeda_destino}'
        
        response = requests.get(url)
        data = response.json()
        
        if data['result'] == 'success':
            taxa = data['conversion_rate']
            return valor * taxa
        else:
            print("Erro ao obter taxa de câmbio:", data.get('error-type', 'Desconhecido'))
            return None
            
    except Exception as e:
        print("Erro na conversão:", str(e))
        return None