SELECT product_id, product_name, total_reviews 
FROM default.rep_product_quality 
ORDER BY total_reviews DESC 
LIMIT 10;