import requests

cep = str(input('insira um cep: ')).replace('-','').replace(' ','').replace('.','')


def localiza():
    if len(cep) == 8:
        try:
            link = f'https://viacep.com.br/ws/{cep}/json/'

            requisicao = requests.get(link)
            print(requisicao.json())

            dicionario = requisicao.json()



            logradouro = dicionario['logradouro']
            bairro = dicionario['bairro']
            localidade = dicionario['localidade']
            uf = dicionario['uf']
            
            print(f'''
            {cep}
            {logradouro}
            {bairro}
            {localidade} - {uf}''')
        
            return localidade, uf
        except:
            print('Desculpa insira o cep novamente!!!')
    elif cep.isalpha() == True or cep.isalnum() == True:
        print('cep inválido tente novamnete')
    else:
        print('insira um cep válido!!!')

localiza()