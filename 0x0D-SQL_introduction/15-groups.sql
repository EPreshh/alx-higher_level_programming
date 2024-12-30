-- lists the number of records with the same acore in 'second_table'
-- result displays the score and number of records
-- for this score with the label number
-- should be sorted by the number of records
-- database name will be passed as an argument to the mysql command
SELECT score, COUNT(*) AS `number`
  FROM `second_table`
  GROUP BY(score)
  ORDER BY `number` DESC;
