-- 3b. Les ventes par produit
SELECT c2 AS ventes_par_produit, SUM(c4) AS quantite_totale 
FROM ventes 
WHERE c1 != 'date' 
GROUP BY c2;