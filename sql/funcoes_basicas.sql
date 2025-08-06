USE sakila;

------------------------------------------

-- FUNÇÕES BÁSICAS DE CONTAGEM

SELECT 
	MAX(amount) AS Maior,
    MIN(amount) AS Menor,
    AVG(amount) AS 'Media de Valores',
    SUM(amount) AS 'Total de Vendas',
    COUNT(amount) AS 'Número de Vendas'
FROM payment
WHERE staff_id = 2;

------------------------------------------

-- AGRUPANDO OS CLIENTES

SELECT
	cus.customer_id AS ID,
    cus.first_name AS Nome,
    cus.last_name AS Sobrenome,
    SUM(amount) AS Total,
    COUNT(amount) AS Compras
FROM payment pay
JOIN customer cus USING(customer_id)
GROUP BY customer_id
HAVING Total >= 150 AND compras >= 35
ORDER BY total DESC;