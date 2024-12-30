-- lists all records with a score >= 10 in 'second_table'
-- ordered by scores in descending order
-- database name will be passed as an argument of the mysql command
SELECT `score`, `name`
  FROM `second_table`
  WHERE `score` >= 10
  ORDER BY `score` DESC;
