SELECT supplier_country, sum(total_revenue) AS country_revenue 
FROM default.rep_suppliers 
GROUP BY supplier_country 
ORDER BY country_revenue DESC;