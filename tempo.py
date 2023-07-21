
import requests





def tempo_descricao(cidade, estado):
    
    try:
        API_KEY = '38ec47181b6d7651fde9444fb2806b8c'
        cidade =  str(cidade).lower()
        estado = str(estado).lower()
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao = dicionaio_requisicao['weather'][0]['description'] 
        umidade = dicionaio_requisicao['main']['humidity']
        temperatura_kelvin = dicionaio_requisicao['main']['temp_min']
        temperatura = str(int(temperatura_kelvin - 273.15))
        vento = dicionaio_requisicao['wind']['speed']
        
        return descricao
    except:
        print(cidade, estado)
        print('não consegui locaizar')

def tempo_umidade(cidade, estado):
    
    try:
        API_KEY = '38ec47181b6d7651fde9444fb2806b8c'
        cidade =  str(cidade).lower()
        estado = str(estado).lower()
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao = dicionaio_requisicao['weather'][0]['description'] 
        umidade = dicionaio_requisicao['main']['humidity']
        temperatura_kelvin = dicionaio_requisicao['main']['temp_min']
        temperatura = str(int(temperatura_kelvin - 273.15))
        vento = dicionaio_requisicao['wind']['speed']
        
        return umidade
    except:
        print(cidade, estado)
        print('não consegui locaizar')

def tempo_temperatura_min(cidade, estado):
    
    try:
        API_KEY = '38ec47181b6d7651fde9444fb2806b8c'
        cidade =  str(cidade).lower()
        estado = str(estado).lower()
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao = dicionaio_requisicao['weather'][0]['description'] 
        umidade = dicionaio_requisicao['main']['humidity']
        temperatura_kelvin = dicionaio_requisicao['main']['temp_min']
        temperatura = str(int(temperatura_kelvin - 273.15))
        vento = dicionaio_requisicao['wind']['speed']

        return temperatura
    except:
        print(cidade, estado)
        print('não consegui locaizar')

def tempo_temperatura_max(cidade, estado):
    
    try:
        API_KEY = '38ec47181b6d7651fde9444fb2806b8c'
        cidade =  str(cidade).lower()
        estado = str(estado).lower()
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao = dicionaio_requisicao['weather'][0]['description'] 
        umidade = dicionaio_requisicao['main']['humidity']
        temperatura_kelvin = dicionaio_requisicao['main']['temp_max']
        temperatura = str(int(temperatura_kelvin - 273.15))
        vento = dicionaio_requisicao['wind']['speed']

        return temperatura
    except:
        print(cidade, estado)
        print('não consegui locaizar')



def tempo_vento(cidade, estado):
    
    try:
        API_KEY = '38ec47181b6d7651fde9444fb2806b8c'
        cidade =  str(cidade).lower()
        estado = str(estado).lower()
        link_api = f'https://api.openweathermap.org/data/2.5/weather?q={cidade},{estado}&appid={API_KEY}&lang=pt_br'
        requisicao = requests.get(link_api)
        dicionaio_requisicao = requisicao.json()
        descricao = dicionaio_requisicao['weather'][0]['description'] 
        umidade = dicionaio_requisicao['main']['humidity']
        temperatura_kelvin = dicionaio_requisicao['main']['temp_min']
        temperatura = str(int(temperatura_kelvin - 273.15))
        vento = dicionaio_requisicao['wind']['speed']
        
        return vento
    except:
        print(cidade, estado)
        print('não consegui locaizar')



def simbolo(cidade,estado):
    descricao = str(tempo_descricao(cidade, estado))
    
    if 'ensolarado' in descricao:
        return '2600'
    elif ' moderada' in descricao:
        return '1F326' 
    elif 'nublado' in descricao:
        return '26C5'
    elif 'nuvens' in descricao:
        return '2601'
    elif 'forte' in descricao:
        return '1F329'
    elif 'leve' in descricao:
        return '2614'
    else:
        return '1F3F3'
