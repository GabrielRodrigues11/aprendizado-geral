USE carros;

------------------------------

-- https://www.w3schools.com/sql/sql_datatypes.asp <--- Data types

-- CRIA TABELA 'marcas'

CREATE TABLE marcas (
	id INT NOT NULL AUTO_INCREMENT,
    nome_marca VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

------------------------------

-- ADICIONA 'origem' A TABELA 'marcas'

ALTER TABLE marcas ADD origem VARCHAR(255);

------------------------------

-- CRIA TABELA 'inventario'

CREATE TABLE inventario (
	id INT NOT NULL AUTO_INCREMENT,
    modelo VARCHAR(255) NOT NULL,
    transmissao VARCHAR(255) NOT NULL,
    motor VARCHAR(255) NOT NULL,
    combustivel VARCHAR(255) NOT NULL,
    marcas_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (marcas_id) REFERENCES marcas(id)
);

------------------------------

-- CRIA TABELA 'clientes'

CREATE TABLE clientes (
	id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

------------------------------

-- INSERÇÃO DE DADOS

INSERT INTO clientes(nome, sobrenome, endereco)
VALUES 
	('Gabriel', 'Rodrigues', 'Rua Vitória'),
    ('Karol', 'Oliveira', 'Rua Amarela'),
    ('João', 'Romano', 'Rua São Paulo'),
    ('Erick', 'Falqueto', 'Rua das Acácias'),
    ('Rafael', 'Pereira', 'Rua das Rosas');

INSERT INTO marcas(nome_marca, origem)
VALUES 
	('BMW', 'Alemanha'),
    ('Fiat', 'Italia'),
    ('Mercedes-Bens', 'Alemanha'),
    ('Renault', 'Franca'),
    ('Jaguar', 'Inglaterra');

INSERT INTO inventario(modelo, transmissao, motor, combustivel, marcas_id)
VALUES 
	('BMW 218', 'Automatica', '2.0', 'Gasolina', 1),
    ('XE 2.0D', 'Manual', '2.0', 'Diesel', 5);
















