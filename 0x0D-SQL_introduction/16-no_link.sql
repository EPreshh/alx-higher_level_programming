-- lists all records of the table 'second_table'
-- rows without a name value should be ommitted
-- results display score and name
-- records listed by descending score
-- database name will be passed as an argument to the mysql command
SELECT `score`, `name`
  FROM `second_table`
  WHERE `score` IS NOT NULL AND `name` IS NOT NULL
  ORDER BY `score` DESC;
