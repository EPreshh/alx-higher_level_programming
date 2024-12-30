-- lists all the records of the table 'second_table'
-- results display both score and the name ordered by score
-- database name will be passed as an argument of the mysql command
SELECT `score`, `name` 
  FROM `second_table`
  ORDER BY `score` DESC;
