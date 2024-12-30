-- computes the score average of all records in 'second_table'
-- result column name is average
-- database name will be passed as an argument of the mysql command
SELECT AVG(score) AS average
  FROM `second_table`;
