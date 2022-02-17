SELECT ProductName
FROM Product
WHERE Id IN (
   SELECT ProductId
   FROM OrderItem
   WHERE Quantity > 100
)