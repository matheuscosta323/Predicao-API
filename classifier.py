import joblib
import numpy as np

# Carrega o modelo uma única vez quando a aplicação inicia
model = joblib.load('models/modelo_aprovacao.pkl')

def prever_aprovacao(idade, Medu, Fedu, traveltime, studytime, failures,
                     famrel, freetime, goout, Dalc, Walc, health, absences,
                     schoolsup, famsup, paid, activities, nursery, higher,
                     internet, romantic):

    # Monta o array com os dados na mesma ordem que o modelo foi treinado
    caracteristicas = np.array([[
        idade, Medu, Fedu, traveltime, studytime, failures,
        famrel, freetime, goout, Dalc, Walc, health, absences,
        schoolsup, famsup, paid, activities, nursery, higher,
        internet, romantic
    ]])

    predicao = model.predict(caracteristicas)

    if predicao[0] == 1:
        return "✅ Aprovado"
    else:
        return "❌ Reprovado"
