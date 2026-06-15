import joblib
import numpy as np

# Carrega o modelo uma única vez quando a aplicação inicia
model = joblib.load('models/modelo_aprovacao.pkl')

def prever_aprovacao(absences, failures, goout, age, health, freetime):

    caracteristicas = np.array([[absences, failures, goout, age, health, freetime]])

    predicao = model.predict(caracteristicas)

    if predicao[0] == 1:
        return "✅ Aprovado"
    else:
        return "❌ Reprovado"
