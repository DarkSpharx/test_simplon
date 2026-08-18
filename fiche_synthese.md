Fiche synthèse des résultats d’analyse obtenus

3a. le chiffre d'affaires total
- requête
SELECT sum(c3 * c4) AS chiffre_d_affaires_total FROM ventes;
- résultat
chiffre_d_affaires_total	44825


3b. les ventes par produit
- requêtes
SELECT c2 AS ventes_par_produit, SUM(c4) AS quantite_totale 
FROM vente 
WHERE c1 != 'date' 
GROUP BY c2;
- résultat
Produit A	1750
Produit B	1055
Produit C	575

3c. les ventes par région.
- requête
SELECT c5 as region,
sum(c3 *c4) as ventes_par_region
FROM ventes
WHERE c1 != 'date'
GROUP BY c5;
- résultat
Nord	20725
Sud	24100