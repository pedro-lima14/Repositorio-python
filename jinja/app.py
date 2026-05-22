from flask import render_template, Flask as f

app = f(__name__)

@app.route('/')
def home():
    nome = "Turma de Python"
    return render_template('index.html', nome=nome)

@app.route('/alunos')
def alunos():
    lista_alunos = [
        {'nome': 'Pedro', 'nota': 12},
        {'nome': 'Lucas', 'nota': 11},
        {'nome': 'Maria', 'nota': 3}
    ]
    return render_template('alunos.html', alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)