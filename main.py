from flask import Flask,render_template,request
import tempo

app = Flask(__name__)


@app.route('/')
def home(): 
    
    return render_template('home.html')
    


@app.route('/inform_tempo', methods = ['GET','POST'])
def ver_tempo():
    
    cidade = str(request.args.get('procura_cidade')).strip()
    estado = str(request.args.get('procura_estado')).strip()

    nome_cidade = cidade.title()
    nome_estado = estado.title()
    descricao = tempo.tempo_descricao(cidade,estado)
    temperatura_min = tempo.tempo_temperatura_min(cidade,estado)
    temperatura_max = tempo.tempo_temperatura_max(cidade,estado)
    umidade = tempo.tempo_umidade(cidade,estado)
    vento = tempo.tempo_vento(cidade,estado)
    simbolo = tempo.simbolo(cidade,estado)
    


    return render_template('tempo_cidade.html',nome_cidade=nome_cidade,nome_estado=nome_estado,temperatura_min=temperatura_min,temperatura_max=temperatura_max,descricao=descricao,umidade=umidade,vento=vento,simbolo=simbolo)


    
if __name__ == '__main__':
    app.run(debug=True)
