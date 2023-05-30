// View all nodes
MATCH (n) RETURN n

// View properties in the properties section
MATCH (n) WHERE (n.property) IS NOT NULL 
RETURN DISTINCT "node" as entity, n.property AS property LIMIT 25 
UNION ALL 
MATCH ()-[r]-() WHERE (r.property) IS NOT NULL 
RETURN DISTINCT "relationship" AS entity, r.property AS property LIMIT 25

// View properties in the properties section
MATCH (n) WHERE (n.property) IS NOT NULL 
RETURN DISTINCT "node" as entity, n.property AS property LIMIT 25 
UNION ALL 
MATCH ()-[r]-() WHERE (r.property) IS NOT NULL 
RETURN DISTINCT "relationship" AS entity, r.property AS property LIMIT 25