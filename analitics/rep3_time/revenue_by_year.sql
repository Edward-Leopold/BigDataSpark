SELECT year, sum(total_revenue) AS yearly_revenue 
FROM default.rep_time 
GROUP BY year;