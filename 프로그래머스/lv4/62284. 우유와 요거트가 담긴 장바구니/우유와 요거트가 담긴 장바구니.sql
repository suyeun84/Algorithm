SELECT cart_id
FROM   cart_products
WHERE  name = 'yogurt' AND 
       cart_id IN (SELECT cart_id
                  FROM   cart_products
                  WHERE name = 'milk')
GROUP
BY     cart_id
ORDER
BY     cart_id