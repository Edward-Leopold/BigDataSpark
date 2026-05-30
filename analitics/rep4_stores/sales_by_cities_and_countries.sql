SELECT store_country, store_city, sum(total_revenue) AS location_revenue
FROM default.rep_stores 
GROUP BY store_country, store_city 
ORDER BY location_revenue DESC;