-- 3c. Les ventes par région
SELECT c5 as region,
sum(c3 *c4) as ventes_par_region
FROM ventes
WHERE c1 != 'date'
GROUP BY c5;