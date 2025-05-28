# Rapport de Nettoyage – EagleEye Fraud

**Date** : 28/05/2025
**Auteur** : Josué KOFFI

## Étapes réalisées

- Chargement du jeu de données (creditcard.csv)
- Vérification de la taille, des colonnes, des types
- Recherche de valeurs manquantes : **aucune valeur manquante détectée**
- Vérification des valeurs extrêmes
    -**Montant (“Amount”)** :
        Minimum : 0 €
        Maximum : 25 691.16 €
        La majorité des transactions sont inférieures à 100 €, mais quelques transactions dépassent 10 000 €. Ces valeurs sont rares mais plausibles pour des transactions bancaires. Aucun montant négatif ou aberrant n’a été détecté.
    -**Temps (“Time”)** :
        Le champ varie de 0 à 172 792 secondes (~48h), ce qui correspond bien à la durée du dataset (2 jours).
    -**Variables V1 à V28** :
        Pas de valeurs manquantes ni infinies détectées. Quelques valeurs extrêmes (supérieures à |10|) mais cohérentes avec une transformation PCA.
    -**Décision** :
        Aucune valeur extrême anormale n’a été détectée nécessitant une correction ou une suppression.

- Analyse de la variable cible : X transactions normales, Y fraudes

## Décisions

- Jeu de données prêt pour l’analyse exploratoire
- Fichier nettoyé enregistré sous `creditcard_clean.csv`

## Informations sur le dataset

- Transactions bancaires (2 jours, septembre 2013, Europe)
- 284 807 lignes, 492 fraudes (0,17% des transactions)
- Variables : V1 à V28 (PCA), 'Time', 'Amount', 'Class' (cible)
- Pas de valeurs manquantes
- Données hautement déséquilibrées
- Conseil d'évaluation : privilégier AUPRC (Precision-Recall), plutôt qu'accuracy
