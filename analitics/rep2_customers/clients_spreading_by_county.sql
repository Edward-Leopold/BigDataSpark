SELECT country, count(customer_id) AS customers_count, sum(total_spend) AS total_country_spend
FROM default.rep_customers 
GROUP BY country 
ORDER BY total_country_spend DESC;