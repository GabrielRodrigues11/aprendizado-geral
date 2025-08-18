---------------------------------------------

-- USUÁRIOS

USE mysql;

-- Visualizar usuários:

SELECT * FROM user;

-- Sem utilizar o USE antes:

SELECT * FROM mysql.user;

---------------------------------------------

-- CRIAÇÃO DE USUÁRIO

-- Cria o usuário e define a senha:

CREATE USER ana IDENTIFIED BY 'senhateste'; 

-- Cria o usuário com FRILTRO - (Só consegue acessar o banco se estiver no localhost)

CREATE USER joao@localhost IDENTIFIED BY 'senhateste';

-- Cria o usuário com FRILTRO - (Só consegue acessar o banco se estiver na empresa dela)

CREATE USER karol@tekeat.com IDENTIFIED BY 'senhateste';

---------------------------------------------

-- REMOÇÃO DE USUÁRIO

DROP USER karol@tekeat.com;

---------------------------------------------

-- RECUPERANDO/TROCAR A SENHA

-- Senha de outro usuário:

SET PASSWORD FOR joao@localhost = 'novasenhateste';

-- Senha do usuário que está logado:

SET PASSWORD = '';

---------------------------------------------

-- PRIVILÉGIOS

-- Adiciona os privilégios para o usuário:

GRANT SELECT, INSERT, UPDATE, DELETE -- <- Habilita tudo isso
ON sakila.* -- <- Escolhe a database e quais tabelas
TO ana; -- <- Escolhe o usuário

-- Verifica os privilégios do usuário:

SHOW GRANTS FOR ana;

-- CRIANDO UM ADM

-- Admin de uma database

GRANT ALL
ON sakila.* 
TO ana; 

SHOW GRANTS FOR ana;

-- Admin de todos databases

GRANT ALL
ON *.* 
TO joao@localhost; 

SHOW GRANTS FOR joao@localhost;

---------------------------------------------

-- REMOVER PRIVILÉGIOS

CREATE USER karol IDENTIFIED BY 'senhateste';

SHOW GRANTS FOR karol;

GRANT SELECT, INSERT, UPDATE
ON sakila.*
TO karol;

REVOKE UPDATE -- <- Remove o UPDATE 
ON sakila.*
FROM karol; -- <- Para remover utilizamos o FROM 