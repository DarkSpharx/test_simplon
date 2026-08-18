import pandas as pd
import plotly.express as px

# 1. Chargement des données
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
donnees = pd.read_csv(url)

# 2. Calcul du Chiffre d'Affaires par ligne (Prix * Quantité)
donnees['ca'] = donnees['prix'] * donnees['qte']

# 3. Création du graphique en camembert
figure = px.pie(
    donnees,
    values='ca',
    names='produit',
    title="Chiffre d'affaires par produit"
)

# 4. Export de la page HTML
figure.write_html('chiffre-d-affaires-par-produit.html')

print("Fichier 'chiffre-d-affaires-par-produit.html' généré avec succès !")