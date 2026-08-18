import pandas as pd
import plotly.express as px

# 1. Chargement des données
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
donnees = pd.read_csv(url)

# 2. Création du graphique en camembert
figure = px.pie(
    donnees,
    values='qte',
    names='produit',
    title='Quantités vendues par produit'
)

# 3. Export de la page HTML
figure.write_html('ventes-par-produit.html')

print("Fichier 'ventes-par-produit.html' généré avec succès !")