-- Show max temperature an state has ever had
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
