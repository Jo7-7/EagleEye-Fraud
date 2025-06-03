import pandas as pd
import joblib

# Charger les données originales
df = pd.read_csv('../data/creditcard_clean.csv')

model = joblib.load('../models/xgboost_fraude.pkl')

# Séparer les features (X)
X = df.drop('Class', axis=1)

# Prédire la fraude (0 ou 1)
df['Fraud_Predicted'] = model.predict(X)

# (Optionnel) Calculer la probabilité de fraude (pour affichage avancé dans Power BI)
df['Fraud_Probability'] = model.predict_proba(X)[:, 1]

# Sauvegarder le dataset scoré
df.to_csv('../data/creditcard_scored.csv', index=False)
