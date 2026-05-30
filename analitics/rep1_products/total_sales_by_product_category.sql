SELECT product_category, sum(total_revenue) AS category_revenue 
FROM default.rep_products 
GROUP BY product_category 
ORDER BY category_revenue DESC;