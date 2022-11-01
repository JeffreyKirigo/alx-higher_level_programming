-- Number of record with same record desc
SELECT score, COUNT(score) AS `number` FROM second_table GROUP BY score;
