from flask import Flask, request, render_template_string

app = Flask(__name__)

usuarios_permitidos = [
    {"usuario": "marcos", "senha": "cotemig2026"},
    {"usuario": "janaina", "senha": "cotemig2026"},
    {"usuario": "pedro", "senha": "12402427"} 
]

def show_the_login_form(mensagem=""):
    
    return render_template_string(f"""
        <h2>Login - Atividade 5</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário" required><br><br>
            <input type="password" name="senha" placeholder="Senha" required><br><br>
            <button type="submit">Entrar</button>
        </form>
        <p style="color: red; font-weight: bold;">{mensagem}</p>
    """)

def do_the_login():
    usuario_digitado = request.form.get('usuario')
    senha_digitada = request.form.get('senha')
    
    login_valido = False

    for credencial in usuarios_permitidos:
        if credencial["usuario"] == usuario_digitado and credencial["senha"] == senha_digitada:
            login_valido = True
            break 

    if login_valido:
        return f"<h1>Acesso permitido! Bem-vindo, {usuario_digitado}.</h1>"
    else:
        
        return show_the_login_form(mensagem="Usuário ou senha incorretos!")


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)

