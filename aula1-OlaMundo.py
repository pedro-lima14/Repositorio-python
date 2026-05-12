from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'O que é: Um decorator é uma função que envolve outra função para estender ou modificar o comportamento dela sem alterar seu código original.Para que serve: Serve para reaproveitar código de forma limpa. É usado para tarefas que se repetem em várias partes do sistema, como controle de acesso, logs ou criação de rotas.Uso no Flask (@app.route): O decorator associa uma URL do navegador a uma função Python. Ele registra a função no sistema interno do Flask para que ela seja executada automaticamente sempre que o endereço correspondente for acessado.' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
