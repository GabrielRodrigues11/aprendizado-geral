USE sakila;

-- BETWEEN
SELECT * FROM payment
WHERE amount BETWEEN 1.99 AND 3.99; -- FILTRA NÚMEROS ENTRE 1.99 E 3.99

---------------------------------------------

-- LIKE
SELECT * FROM actor
WHERE first_name LIKE 'alb%'; -- FIRST_NAME QUE CONTÉM 'ALB'

SELECT * FROM actor
WHERE first_name LIKE '%c'; -- FIRST_NAME QUE TERMINA COM 'C'

/*
 Alguns exemplos:
'abc' LIKE 'abc'    verdade
'abc' LIKE 'a%'     verdade
'abc' LIKE '_b_'    verdade
'abc' LIKE 'c'      falso
*/
---------------------------------------------

-- IS NULL

SELECT * FROM address
WHERE address2 IS NULL; -- FILTRA OS ADDRESS2 NULOS

---------------------------------------------

-- LIMIT

SELECT * FROM actor
LIMIT 99, 10; -- PULA ATÉ O ACTOR_ID 100 E CONTÁ OS PRÓXIMOS 10

---------------------------------------------

-- REGEXP

SELECT * FROM actor
WHERE first_name REGEXP 'a'; -- Contém a letra 'a'

SELECT * FROM actor
WHERE first_name REGEXP '^a'; -- Começa com a letra 'a'

SELECT * FROM actor
WHERE first_name REGEXP '^a|^d|^r'; -- Começa com a letra 'a' OU 'd' OU 'r'

SELECT * FROM actor
WHERE first_name REGEXP '[ger]a'; -- Contém 'ga' OU 'ea' OU 'ra'


SELECT * FROM actor
WHERE first_name REGEXP '^[ger]a'; -- Inicia com 'ga' ou 'ea' ou 'ra'

--------------------------------------------- 

-- INNER JOIN

SELECT * FROM customer
JOIN payment ON customer.customer_id = payment.payment_id; -- Juntando a tabela customer + payment

-- Filtrando as colunas

SELECT 
    cus.customer_id,
    cus.first_name,
    cus.last_name,
    pay.rental_id,
    pay.amount
FROM customer cus --  <--- Aqui é um ALIAS (apelido) no caso eu abreviei o 'customer' para 'cus', assim, o código fica MAIS LIMPO!.
JOIN payment pay ON cus.customer_id = pay.payment_id; -- O customer_id tem que ser igual ao payment_id, se não, as informações estarão erradas

-- Adicionando mais tabelas

SELECT 
    cus.customer_id,
    cus.first_name,
    cus.last_name,
    adr.address,
    pay.rental_id,
    pay.amount
FROM customer cus
JOIN payment pay
    ON cus.customer_id = pay.payment_id
JOIN address adr
    ON cus.customer_id = adr.address_id;
    
---------------------------------------------

-- CRIAR UMA TABELA

CREATE TABLE payment_backup AS
SELECT * FROM payment;

-- ATUALIZAR UM REGISTRO

UPDATE payment
SET
	amount = 15.99
WHERE 
	payment_id = 1;
    
-- APAGAR UM REGISTRO

DELETE FROM payment
WHERE payment_id = 16049;