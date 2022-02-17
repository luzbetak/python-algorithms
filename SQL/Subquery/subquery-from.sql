SELECT AVG(rate)
FROM (
    SELECT rate
    FROM bank.interest
    WHERE dt >= (NOW() - INTERVAL 1 MONTH)
    ORDER BY rate DESC
    LIMIT 20000
) a
