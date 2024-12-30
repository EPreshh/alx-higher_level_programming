-- updates the sscore of Bob to 10 in the 'second_table'
-- only using the name field
-- database name will be passed as an argument of the mysql command
UPDATE `second_table`
  SET `score` = 10
  WHERE `name` = 'Bob';
