import requests

cep = str(input('insira um cep: ')).replace('-','').replace(' ','').replace('.','')


def localiza():
    if len(cep) == 8:
        try:
            link = f'https://viacep.com.br/ws/{cep}/json/'

            requisicao = requests.get(link)
            dicionario = requisicao.json()



            logradouro = dicionario['logradouro']
            bairro = dicionario['bairro']
            localidade = dicionario['localidade']
            uf = dicionario['uf']
        
            return {"status_code": 200, "menssage": "Cep válido", "loalidade": localidade, "estado": uf}
        except:
            return {"status_code": 500, "menssage": "Erro interno do servidor"}
    elif cep.isalpha() == True or cep.isalnum() == True:
        return {"error_status": 400, "menssage": "Cep inválido"}
    else:
        return {"status_code": 400, "menssage": "Cep inválido"}

localiza()
