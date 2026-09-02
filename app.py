from flask import Flask, render_template, request
from api import obter_cotacao

#para conseguir os simbolos das moedas eu pesquisei os simbolos na internet
moedas = {
    "USD-BRL": "US$",
    "EUR-BRL": "€",
    "JPY-BRL": "¥"}

app = Flask(__name__)

@app.route ("/", methods=["GET", "POST"])
def inicio():

    cotacao = None
    resultado = None
    simbolo = None
    erro = None

    if request.method == "POST":

        try:
            valor = float(request.form["valor"])

            if valor <= 0:
                erro = "Digite um valor positivo para o calculo."
            
            else:    
                moeda = request.form["moeda"]

                cotacao = obter_cotacao(moeda)

                if cotacao is None:
                    erro = "Não foi possível obter a cotação no momento. Tente novamente mais tarde."

                else:

                    resultado = valor / cotacao

                    simbolo = moedas[moeda]

        except ValueError:
            erro = "Digite um valor válido."


    return render_template("index.html", cotacao=cotacao, resultado=resultado, simbolo=simbolo, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)