import pandas as pd
import plotly.express as px

# 1. Chargement des données
# On lit le fichier CSV depuis l'URL et on le stocke dans un tableau (donnees)
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
donnees = pd.read_csv(url)

# 2. Création du camembert
# px.pie = fabrique un graphique en camembert
figure = px.pie(
    donnees,             # Le tableau de données source
    values='qte',       # La colonne chiffrée pour calculer la taille des parts
    names='produit',    # La colonne texte pour nommer chaque tranche
    title='Quantités vendues par produit' # Le titre du graphique
)

# 3. Export en page web
# On sauvegarde le graphique dans un fichier HTML interactif
figure.write_html('ventes-par-produit.html')

print("Fichier 'ventes-par-produit.html' généré avec succès !")