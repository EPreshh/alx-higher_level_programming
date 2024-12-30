-- Creates a table in current database if it it doesn't exist
-- Database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS first_table(
  id INT,
  name VARCHAR(256)
  );
