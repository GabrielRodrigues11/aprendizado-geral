------------------------------

-- STRINGS

-- https://dev.mysql.com/doc/refman/8.4/en/string-functions.html <- Todas as funções de String.

SELECT TRIM(BOTH 'a' FROM 'aaaaaaaCarrosaaaaaaaaaa'); -- RETIRA TODOS OS 'a'

SELECT TRIM(LEADING 'a' FROM 'aaaaaaaCarrosaaaaaaaaaa'); -- RETIRA TODOS OS 'a' ANTES DO 'Carros'

SELECT TRIM(TRAILING 'a' FROM 'aaaaaaaCarrosaaaaaaaaaa');-- RETIRA TODOS OS 'a' DEPOIS DO 'Carros'

SELECT LOCATE('o', 'Carros'); -- QUAL POSIÇÃO ESTÁ O 'o'

SELECT LOCATE('c', 'Carros'); -- QUAL POSIÇÃO ESTÁ O 'C'

SELECT lcase('CARRos'); -- TRANSFORMA EM MINUSCULO 

SELECT ucase('CARRos'); -- TRANSFORMA EM MINUSCULO

SELECT length('CARRos'); -- CONTA AS CARACTERES

SELECT REPEAT('CARRos', '4'); -- REPETE A PALAVRA

SELECT RIGHT('CARRos', '4'); --  MOSTRA AS ÚLTIMAS 4 LETRAS (DIREITA)

SELECT LEFT('CARRos', '4'); --  MOSTRA AS PRIMEIRAS 4 LETRAS (ESQUERDA)

SELECT LEFT('CARRos', '4'); --  MOSTRA AS PRIMEIRAS 4 LETRAS (ESQUERDA)