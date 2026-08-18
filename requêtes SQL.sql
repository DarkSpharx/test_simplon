-- 3a. le chiffre d'affaires total
SELECT sum(c3 * c4) AS chiffre_d_affaires_total FROM ventes;

-- 3b. Les ventes par produit
SELECT c2 AS ventes_par_produit, SUM(c4) AS quantite_totale 
FROM ventes 
WHERE c1 != 'date' 
GROUP BY c2;

-- 3c. Les ventes par région
SELECT c5 as region,
sum(c3 *c4) as ventes_par_region
FROM ventes
WHERE c1 != 'date'
GROUP BY c5;