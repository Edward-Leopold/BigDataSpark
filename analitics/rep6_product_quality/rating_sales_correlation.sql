SELECT avg_rating, sum(sales_quantity) AS total_sold 
FROM default.rep_product_quality 
GROUP BY avg_rating 
ORDER BY avg_rating DESC;