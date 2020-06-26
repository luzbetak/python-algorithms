-- Find the pair of actors who have worked in maximum number of movies together

-- INPUT - movie_table
-- movie_id | actor_id
-- ---------+----------
--    100   |    1
--    100   |    2
--    100   |    3
--    200   |    1
--    200   |    3
--    200   |    4
--    300   |    1
--    300   |    2

DROP TABLE movie_table;
CREATE TABLE IF NOT EXISTS movie_table (
	movie_id INTEGER,
	actor_id INTEGER
);

INSERT INTO movie_table VALUES(10,1);
INSERT INTO movie_table VALUES(10,2);
INSERT INTO movie_table VALUES(10,3);

INSERT INTO movie_table VALUES(20,1);
INSERT INTO movie_table VALUES(20,3);
INSERT INTO movie_table VALUES(20,4);

INSERT INTO movie_table VALUES(30,1);
INSERT INTO movie_table VALUES(30,2);
INSERT INTO movie_table VALUES(30,3);

SELECT t1.actor_id AS actor1, t2.actor_id AS actor2, count(t1.movie_id) AS total_movies
FROM movie_table t1, movie_table t2
    ON t1.movie_id = t2.movie_id
    AND t1.actor_id < t2.actor_id
GROUP BY actor1, actor2
ORDER BY total_movies DESC

-- OUTPUT TABLE
-- actor1 | actor2 | total_movies
-- -------+--------+--------------
--    1   |    1   |      3
--    1   |    2   |      2
--    2   |    3   |      2
--    1   |    1   |      1
--    3   |    4   |      1

