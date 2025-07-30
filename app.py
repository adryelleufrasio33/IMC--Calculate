from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif  25 <= imc <=29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc <= 39.9:
        return "Obesidade Grau 2"
    else:
        return "Morbido"
    
@app.route("/nova")
def nome():
    return "teste de rota"


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        try:
            nome = request.form["nome"]
            peso = float(request.form["peso"])
            altura = float(request.form["altura"])
            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)
            resultado = {
                "nome": nome,
                "peso": peso,
                "altura": altura,
                "imc": round(imc, 2),
                "classificacao": classificacao
            }
        except (KeyError, ValueError):
            return "Erro nos dados enviados pelo formulário", 400

    return render_template("index.html", resultado=resultado)


# Rota para formulario de paciente
@app.route("/cadastro_paciente", methods=["GET", "POST"])
def cadastro_paciente():
    Mensagem = None
    if request .method == "POST":
        nome = request.form["Nome"]
        idade = request.form["Idade"]   
        especialista = request.form["Especialista"]
        Mensagem = (f"Paciente {nome},({idade} anos), marcado para {especialista}")
        return render_template("cadastrar_paciente.html", Mensagem=Mensagem)
    return render_template("cadastrar_paciente.html")

if __name__ == "__main__":
    app.run(debug=True)