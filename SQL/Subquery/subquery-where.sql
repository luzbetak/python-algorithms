SELECT *
FROM t1
WHERE column1 = (SELECT column1 FROM t2);
