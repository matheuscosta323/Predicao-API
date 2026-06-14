from flask import Flask, request, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

from classifier import prever_aprovacao

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        # Coleta os dados do formulário
        idade       = int(request.form.get("age"))
        Medu        = int(request.form.get("Medu"))
        Fedu        = int(request.form.get("Fedu"))
        traveltime  = int(request.form.get("traveltime"))
        studytime   = int(request.form.get("studytime"))
        failures    = int(request.form.get("failures"))
        famrel      = int(request.form.get("famrel"))
        freetime    = int(request.form.get("freetime"))
        goout       = int(request.form.get("goout"))
        Dalc        = int(request.form.get("Dalc"))
        Walc        = int(request.form.get("Walc"))
        health      = int(request.form.get("health"))
        absences    = int(request.form.get("absences"))
        schoolsup   = int(request.form.get("schoolsup"))
        famsup      = int(request.form.get("famsup"))
        paid        = int(request.form.get("paid"))
        activities  = int(request.form.get("activities"))
        nursery     = int(request.form.get("nursery"))
        higher      = int(request.form.get("higher"))
        internet    = int(request.form.get("internet"))
        romantic    = int(request.form.get("romantic"))

        # Faz a predição
        resultado = prever_aprovacao(
            idade, Medu, Fedu, traveltime, studytime, failures,
            famrel, freetime, goout, Dalc, Walc, health, absences,
            schoolsup, famsup, paid, activities, nursery, higher,
            internet, romantic
        )

        # Gráfico de barras com as variáveis mais relevantes enviadas
        dados = pd.DataFrame({
            'Variável': ['Reprovações', 'Tempo de Estudo', 'Faltas', 'Álcool (semana)', 'Saídas'],
            'Valor': [failures, studytime, absences, Walc, goout]
        })

        figura = px.bar(
            dados,
            x='Variável',
            y='Valor',
            title='Resumo das Variáveis do Aluno',
            color='Variável'
        )
        grafico = pio.to_html(figura, full_html=False)

        return render_template('index.html', predicao=resultado, grafico=grafico)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
