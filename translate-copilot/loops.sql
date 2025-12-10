-- SQL version (using a simple example)
-- In SQL, iteration is typically done with cursors or recursive CTEs
-- Here's a basic example with a CTE:

WITH fruits AS (
    SELECT 'apple' as fruit
    UNION ALL
    SELECT 'banana'
    UNION ALL
    SELECT 'pear'
)
SELECT CONCAT('I like ', fruit) as message
FROM fruits;
