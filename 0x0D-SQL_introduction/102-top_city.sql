-- script to display top 3 cities with the highest average temperature from JULY to AUGUST
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;