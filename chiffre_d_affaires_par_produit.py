import pandas as pd
import plotly.express as px

# 1. Chargement des données
# On lit le fichier CSV depuis l'URL et on le stocke dans un tableau (donnees)
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv'
donnees = pd.read_csv(url)

# 2. Calcul du Chiffre d'Affaires
# On crée une nouvelle colonne 'ca' en multipliant le prix par la quantité pour chaque ligne
donnees['ca'] = donnees['prix'] * donnees['qte']

# 3. Création du camembert
# px.pie = fabrique un graphique en camembert
figure = px.pie(
    donnees,                                # Le tableau de données source
    values='ca',                            # La colonne du chiffre d'affaires calculé (taille des parts)
    names='produit',                        # La colonne texte pour nommer chaque tranche
    title="Chiffre d'affaires par produit"  # Le titre du graphique
)

# 4. Export en page web
# On sauvegarde le graphique dans un fichier HTML interactif
figure.write_html('chiffre-d-affaires-par-produit.html')

print("Fichier 'chiffre-d-affaires-par-produit.html' généré avec succès !")