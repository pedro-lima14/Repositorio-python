from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('index.html') 


@app.route('/cotemig/<nome>') 
def cotemig(nome):
    return f"<h1>Olá {nome}, seja bem vindo!</h1>"


if __name__ == '__main__':
    app.run(debug=True) 