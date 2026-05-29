import math

from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "log":
        base_valor = request.form.get("num2", "").strip()
        base = float(base_valor) if base_valor else 10.0
        
        if num1 <= 0 or base <= 0 or base == 1:
            resultado = "Erro"
            etapas = "O número e a base devem ser maiores que 0. A base não pode ser 1."
        else:
            resultado = math.log(num1, base)
            etapas = f"log na base {base} de {num1} = {resultado}"

    elif operacao == "bhaskara":
        valores_bc = request.form.get("num2", "").strip()
        if not valores_bc or "," not in valores_bc:
            resultado = "Erro"
            etapas = "Para Bhaskara, digite os valores de b e c separados por vírgula no segundo campo. Ex: 5,6"
        else:
            try:
                b_str, c_str = valores_bc.split(",")
                a = num1
                b = float(b_str.strip())
                c = float(c_str.strip())
                
                if a == 0:
                    resultado = "Erro"
                    etapas = "O coeficiente 'a' não pode ser 0 em equação de 2º grau."
                else:
                    delta = (b ** 2) - (4 * a * c)
                    if delta < 0:
                        resultado = "Sem raízes reais"
                        etapas = f"Δ = {delta} (negativo)"
                    else:
                        x1 = (-b + math.sqrt(delta)) / (2 * a)
                        x2 = (-b - math.sqrt(delta)) / (2 * a)
                        resultado = f"x1 = {x1} | x2 = {x2}"
                        etapas = f"Δ = {delta} | x = (-({b}) ± √{delta}) / (2·{a})"
            except ValueError:
                resultado = "Erro"
                etapas = "Formato inválido. Digite dois números separados por vírgula. Ex: -5, 6"

    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"
            else:
                resultado = "Erro: Divisão por zero"
                etapas = "Não é possíve dividir por zero"
        elif operacao == "**":
            resultado = num1 ** num2 
            etapas = f"{num1} ** {num2} = {resultado}"
        else:
            resultado = "Operação inválida"
            etapas = "A opção seleionada é inválida"

    return render_template ("calculadora.html", etapas=etapas, resultados=resultado)


