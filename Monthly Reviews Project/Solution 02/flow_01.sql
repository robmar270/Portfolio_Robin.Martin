WITH CompanyNames AS (
  SELECT
    `name` AS company_name,
    id AS metric_id,
    2024 AS target_year,
    3 AS target_month_year_to_date,
    3 AS target_month
  FROM
    companies
  WHERE
    id IN (12)
)

-- Query 1: Total Count Of Transports Last Month 
SELECT
  c.company_name,
  c.metric_id,
  'Last Month Total Count Of Transports' AS metric_name,
  COALESCE(
    (
      SELECT COUNT(*)
      FROM bookings b
      WHERE b.client_id = c.metric_id
        AND YEAR(b.created_at) = c.target_year
        AND MONTH(b.created_at) = c.target_month
    ),
    0
  ) AS metric_value
FROM
  CompanyNames c
  
UNION ALL
-- Query 2: Total Count Of Transports Year-to-Date 
SELECT
  c.company_name,
  c.metric_id,
  'Year-to-Date Total Count Of Transports' AS metric_name,
  COALESCE(
    (
      SELECT COUNT(*)
      FROM bookings b
      WHERE b.client_id = c.metric_id
        AND YEAR(b.created_at) = c.target_year
        AND MONTH(b.created_at) <= c.target_month_year_to_date
    ),
    0
  ) AS metric_value
FROM
  CompanyNames c
  

UNION ALL
-- Query 2: Total Deliveries not on Time (Last Month)
SELECT
  c.company_name,
  c.metric_id,
  'Total Deliveries not on Time (Month)' COLLATE utf8mb4_general_ci AS metric_name,
  COALESCE(
    CONCAT(ROUND(COALESCE(notQualityCount.notQualityTotal / NULLIF(totalCount.total, 0), 0) * 100, 2), '%'),
    'No data available'
  ) AS metric_value
FROM (
  SELECT
    company_id,
    COUNT(*) AS total
  FROM
    bookings
  WHERE
    YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) = (SELECT target_month FROM CompanyNames LIMIT 1)
    AND company_id = (SELECT metric_id FROM CompanyNames LIMIT 1)  
  GROUP BY
    company_id
) AS totalCount
LEFT JOIN (
  SELECT
    company_id,
    COUNT(*) AS notQualityTotal
  FROM
    bookings
  WHERE
    YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) = (SELECT target_month FROM CompanyNames LIMIT 1)
    AND company_id = (SELECT metric_id FROM CompanyNames LIMIT 1)  
    AND (
      (ABS(TIMESTAMPDIFF(DAY, bookings.delivery_at, goods_delivered_on)) > 0
      AND bookings.deviation_delivery_at IS NULL)
      OR (ABS(TIMESTAMPDIFF(DAY, bookings.deviation_delivery_at, goods_delivered_on)) > 0
      AND bookings.deviation_delivery_at IS NOT NULL)
    )
  GROUP BY
    company_id
) AS notQualityCount ON totalCount.company_id = notQualityCount.company_id
RIGHT JOIN CompanyNames c ON c.metric_id = totalCount.company_id

UNION ALL
-- Total Deliveries not on Time (Year to Date)
SELECT
  c.company_name,
  c.metric_id,
  'Total Deliveries not on Time (Year to Date)' COLLATE utf8mb4_general_ci AS metric_name,
  COALESCE(
    CONCAT(ROUND(COALESCE(notQualityCount.notQualityTotal / NULLIF(totalCount.total, 0), 0) * 100, 2), '%'),
    'No data available'
  ) AS metric_value
FROM (
  SELECT
    company_id,
    COUNT(*) AS total
  FROM
    bookings
  WHERE
    YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) <= (SELECT target_month_year_to_date from CompanyNames LIMIT 1)
    AND company_id = (SELECT metric_id FROM CompanyNames LIMIT 1)  
  GROUP BY
    company_id
) AS totalCount
LEFT JOIN (
  SELECT
    company_id,
    COUNT(*) AS notQualityTotal
  FROM
    bookings
  WHERE
    YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) <= (SELECT target_month_year_to_date from CompanyNames LIMIT 1)
    AND company_id = (SELECT metric_id FROM CompanyNames LIMIT 1)  
    AND (
      (ABS(TIMESTAMPDIFF(DAY, bookings.delivery_at, goods_delivered_on)) > 0
      AND bookings.deviation_delivery_at IS NULL)
      OR (ABS(TIMESTAMPDIFF(DAY, bookings.deviation_delivery_at, goods_delivered_on)) > 0
      AND bookings.deviation_delivery_at IS NOT NULL)
    )
  GROUP BY
    company_id
) AS notQualityCount ON totalCount.company_id = notQualityCount.company_id
RIGHT JOIN CompanyNames c ON c.metric_id = totalCount.company_id 


UNION ALL
-- Query 3 Total Purchase orders DEVIATIONS Created (Month)
SELECT
  c.company_name,
  c.metric_id,
  'Total Purchase Order Deviations Created (Month)' COLLATE utf8mb4_general_ci AS metric_name,
  COALESCE(
    (SELECT COUNT(deviations.id) FROM deviations 
    WHERE deviations.company_id = c.metric_id   
    AND YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) = (SELECT target_month FROM CompanyNames LIMIT 1)),
    0
  ) AS metric_value
FROM
  CompanyNames c
  
UNION ALL
-- Total Purchase orders DEVIATIONS Created (Year)
SELECT
  c.company_name,
  c.metric_id,
  'Total Purchase Order Deviations Created (Year to Date)' COLLATE utf8mb4_general_ci AS metric_name,
  COALESCE(
    (SELECT COUNT(deviations.id) FROM deviations 
    WHERE deviations.company_id = c.metric_id   
    AND YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) <= (SELECT target_month_year_to_date FROM CompanyNames LIMIT 1)),
    0
  ) AS metric_value
FROM
  CompanyNames c
  

UNION ALL
-- Query 4 'Total Purchase Orders Created (Month)
SELECT
  c.company_name,
  c.metric_id,
  'Total Purchase Orders Created (Month)' AS metric_name,
  COALESCE(
    (SELECT COUNT(*) FROM orders 
    WHERE orders.company_id = c.metric_id 
    AND YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) = (SELECT target_month FROM CompanyNames LIMIT 1)),
    0
  ) AS metric_value
FROM
  CompanyNames c

UNION ALL
-- Total Purchase Orders Created (Year)
SELECT
  c.company_name,
  c.metric_id,
  'Total Purchase Orders Created (Year to Date)' AS metric_name,
  COALESCE(
    (SELECT COUNT(*) FROM orders 
    WHERE orders.company_id = c.metric_id 
    AND YEAR(created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(created_at) <= (SELECT target_month_year_to_date FROM CompanyNames LIMIT 1)),
    0
  ) AS metric_value
FROM
  CompanyNames c
    

UNION ALL
-- Query 5: Top Destination Month
SELECT
  c.company_name,
  c.metric_id,
  'Top Destinations (Month)' AS metric_name,
  COALESCE(
    (
      SELECT CONCAT(a.`name`, ', ', COALESCE(a.`state`, ''), ' (', CAST(COUNT(*) AS CHAR), ')') COLLATE utf8mb4_general_ci
      FROM bookings b
      JOIN companies co ON b.client_id = co.id
      JOIN addresses a ON b.ship_to = a.id
      WHERE YEAR(b.created_at) = c.target_year
        AND MONTH(b.created_at) = c.target_month
        AND b.company_id = c.metric_id
        AND b.company_id IS NOT NULL  
      GROUP BY co.`name`, a.`name`, a.`state`
      ORDER BY COUNT(*) DESC
      LIMIT 1
    ),
    'No data available'
  ) AS metric_value
FROM
  CompanyNames c

UNION All
-- Top Destinations Year to date
SELECT
  c.company_name,
  c.metric_id,
  'Top Destinations (Year to Date)' AS metric_name,
  COALESCE(
    (
      SELECT CONCAT(a.`name`, ', ', COALESCE(a.`state`, ''), ' (', CAST(COUNT(*) AS CHAR), ')') COLLATE utf8mb4_general_ci
      FROM bookings b
      JOIN companies co ON b.client_id = co.id
      JOIN addresses a ON b.ship_to = a.id
      WHERE YEAR(b.created_at) = c.target_year
        AND MONTH(b.created_at) <= c.target_month_year_to_date
        AND b.company_id = c.metric_id
        AND b.company_id IS NOT NULL  
      GROUP BY co.`name`, a.`name`, a.`state`
      ORDER BY COUNT(*) DESC
      LIMIT 1
    ),
    'No data available'
  ) AS metric_value
FROM
  CompanyNames c


UNION ALL
-- Query 6 'Total Order Value By Currency (Month)'
SELECT
  c.company_name,
  c.metric_id,
  'Total Order Value By Currency (Month)' COLLATE utf8mb4_general_ci AS metric_name,
  CONCAT(units.`name`, ' ', FORMAT(SUM(orders.total_price), 0, 'sv_SE')) AS metric_value
FROM 
  CompanyNames c
INNER JOIN orders ON c.metric_id = orders.company_id
INNER JOIN companies ON orders.company_id = companies.id
INNER JOIN units ON orders.currency_id = units.id 
WHERE 
    YEAR(orders.created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(orders.created_at) = (SELECT target_month FROM CompanyNames LIMIT 1)
GROUP BY c.company_name, c.metric_id, units.`name`
HAVING SUM(orders.total_price) > 0


UNION ALL
-- Total Order Value By Currency (Year to date)
SELECT
  c.company_name,
  c.metric_id,
  'Total Order Value By Currency (Year to Date)' COLLATE utf8mb4_general_ci AS metric_name,
  CONCAT(units.`name`, ' ', FORMAT(SUM(orders.total_price), 0, 'sv_SE')) AS metric_value
FROM 
  CompanyNames c
INNER JOIN orders ON c.metric_id = orders.company_id
INNER JOIN companies ON orders.company_id = companies.id
INNER JOIN units ON orders.currency_id = units.id
WHERE 
    YEAR(orders.created_at) = (SELECT target_year FROM CompanyNames LIMIT 1)
    AND MONTH(orders.created_at) <= (SELECT target_month_year_to_date FROM CompanyNames LIMIT 1)
GROUP BY c.company_name, c.metric_id, units.`name`
HAVING SUM(orders.total_price) > 0;
