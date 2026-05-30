SELECT customer_name, total_spend 
FROM default.rep_customers 
WHERE customer_rank <= 10 
ORDER BY total_spend DESC;