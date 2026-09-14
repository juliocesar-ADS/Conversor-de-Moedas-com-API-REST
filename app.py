from flask import Flask, render_template, request
from api import obter_cotacao

#lista para armazenar o histórico de conversões
historico = []

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
    valor = None

    if request.method == "POST":

        acao = request.form.get("acao")

        if acao == "limpar_historico":
            historico.clear()
            return render_template(
                "index.html",
                cotacao=None,
                resultado=None,
                simbolo=None,
                erro=None,
                simbolo_de=None,
                valor=None,
                historico=historico
                )

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
                    
            # Adicionar a conversão ao histórico
            if resultado is not None and cotacao is not None:
                historico.append({
                    "valor": valor,
                    "de": de,
                    "simbolo_de": simbolo_de,
                    "para": para,
                    "simbolo": simbolo,
                    "resultado": resultado,
                    "cotacao": cotacao
                })
               

        except ValueError:
            erro = "Digite um valor válido."



    return render_template("index.html", cotacao=cotacao, resultado=resultado, simbolo=simbolo, erro=erro, simbolo_de=simbolo_de, valor=valor, historico=historico)

if __name__ == "__main__":
    app.run(debug=True)