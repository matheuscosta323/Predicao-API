from flask import Flask, request, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

from classifier import prever_aprovacao

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        absences = int(request.form.get("absences"))
        failures = int(request.form.get("failures"))
        goout    = int(request.form.get("goout"))
        age      = int(request.form.get("age"))
        health   = int(request.form.get("health"))
        freetime = int(request.form.get("freetime"))

        resultado = prever_aprovacao(absences, failures, goout, age, health, freetime)

        # Gráfico com os dados do aluno
        dados = pd.DataFrame({
            'Variável': ['Faltas', 'Reprovações', 'Saídas', 'Idade', 'Saúde', 'Tempo Livre'],
            'Valor':    [absences,  failures,      goout,    age,     health,   freetime]
        })

        figura = px.bar(
            dados,
            x='Variável',
            y='Valor',
            title='Perfil do Aluno',
            color='Variável'
        )
        grafico = pio.to_html(figura, full_html=False)

        return render_template('index.html', predicao=resultado, grafico=grafico)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
