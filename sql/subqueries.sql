USE sakila;

------------------------------

-- SUBQUERY

SELECT * FROM payment
WHERE amount > (
	SELECT AVG(amount) 
    FROM payment);

------------------------------

-- UTILIZANDO MAX    

SELECT * FROM payment
WHERE amount = (
	SELECT MAX(amount)
	FROM payment
	WHERE customer_id = 1);
   
------------------------------

-- UTILIZANDO ANY
   
SELECT *
FROM customer
WHERE customer_id IN (
	SELECT customer_id
	FROM payment
	GROUP BY customer_id
	HAVING COUNT(*) > 35);

------------------------------

-- UTILIZANDO ANY

SELECT *
FROM customer
WHERE customer_id = ANY (
	SELECT customer_id
	FROM payment
	GROUP BY customer_id
	HAVING COUNT(*) > 35);