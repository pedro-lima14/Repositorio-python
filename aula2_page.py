from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
        </head>
        <body>
            <h1>Currículo</h1>

            <h2>Informações Pessoais</h2>
            <ul>
                <li><strong>Nome:</strong> Pedro Lima Barbosa de Almeida</li>  
                <li><strong>Email:</strong> 12402427@aluno.cotemig.com.br</li>
                <li><strong>Telefone:</strong> (31) 98468-2645</li>
            </ul>

            <h2>Experiência Profissional</h2>
            <ul>
                <li><strong>Empresa:</strong>ACCE Capital</li>
                <li><strong>Cargo:</strong>Estagiário em processos e sistemas financeiros</li>
                <li><strong>Período:</strong> Mar 2026 - Presente</li>
            </ul>

            <h2>Histórico acadêmico</h2>
            <ul>
                <li><strong>Colégio:</strong>Santa Maria Minas</li>
                <li><strong>Período:</strong> Fev 2012 - Dez 2023</li>
            </ul>
            <ul>
                <li><strong>Colégio:</strong>Cotemig</li>
                <li><strong>Curso:</strong>Curso técnico em TI</li>
                <li><strong>Período:</strong> Fev 2024 - Presente</li>
            </ul>

            <h2>Prêmios</h2>
            <ul>
                <li><strong>Olímpiada canguru de matemática:</strong>Medalista de bronze(2018-2019-2020) Medalhista de ouro(2021)</li>
                <li><strong>Destaque acadêmico Colégio Santa Maria:</strong>2019 - 2020 - 2021</li>
                <li><strong>The best of the class - Cotemig:</strong> 2025</li>
                <li><strong>3° colocado Hackaton AI Agentes - AWS & Canastra Ventures:</strong>2026</li>
            </ul>


        </body>
        </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
