from flask import Flask, render_template, request
from api import obter_cotacao

#para conseguir os simbolos das moedas eu pesquisei os simbolos na internet
moedas = {
    "USD": "US$",
    "EUR": "€",
    "JPY": "¥",
    "BRL": "R$"}

app = Flask(__name__)

@app.route ("/", methods=["GET", "POST"])
def inicio():

    cotacao = None
    resultado = None
    simbolo = None
    erro = None
    simbolo_de = None

    if request.method == "POST":

        try:
            valor = float(request.form["valor"])

            if valor <= 0:
                erro = "Digite um valor positivo para o calculo."
            
            else:    
                de = request.form["de"]
                para = request.form["para"]

                simbolo_de = moedas[de]
                simbolo = moedas[para]

                if de == para:
                    resultado = valor
                    cotacao = 1

                else:
                    cotacao = obter_cotacao(de + "-" + para)

                    if cotacao is None:
                        erro = "Não foi possível obter a cotação no momento. Tente novamente mais tarde."

                    else:

                        resultado = valor * cotacao

        except ValueError:
            erro = "Digite um valor válido."


    return render_template("index.html", cotacao=cotacao, resultado=resultado, simbolo=simbolo, erro=erro, simbolo_de=simbolo_de)

if __name__ == "__main__":
    app.run(debug=True)