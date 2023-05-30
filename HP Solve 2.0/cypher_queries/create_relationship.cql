//count data rows in Dataset-SA.csv (no headers)
LOAD CSV FROM 'file:///Dataset-SA.csv' AS row
RETURN count(row);

//view data rows in Dataset-SA.csv
LOAD CSV FROM 'file:///Dataset-SA.csv' AS row
RETURN row
LIMIT 25;

//count data rows in Dataset-SA.csv (headers)
LOAD CSV WITH HEADERS FROM 'file:///Dataset-SA.csv' AS row
WITH row WHERE row.product_name = 'Germany'
RETURN row
LIMIT 5;

// create a node label (product_name, sentiment)for the properties
CREATE CONSTRAINT UniqueProduct ON (p:Product) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT UniqueOrder ON (o:sentiment) ASSERT o.id IS UNIQUE;

// crete a node label(price, review, rate)
CREATE (node: Review)

LOAD CSV WITH HEADERS FROM 'file:///Dataset-SA.csv' AS row
MERGE (r:Review)
SET r.review = row.review,
    r.id = CASE WHEN row.id IS NULL THEN "" ELSE row.id END



LOAD CSV FROM 'file:///products.csv' AS row
WITH toInteger(row[0]) AS productId, row[1] AS productName
MERGE (p:Product {productId: productId})
  SET p.productName = productName,
RETURN count(p);

//validate products loaded correctly
MATCH (n:product_name) 
RETURN n LIMIT 25;

//validate orders loaded correctly
MATCH (o:Order)
RETURN o LIMIT 20;

MATCH p=()-[r:RELATIONSHIP]->() RETURN p LIMIT 25