CREATE DATABASE tienda;
USE tienda;

-- DROP DATABASE tienda

CREATE TABLE categoria(
id_cat INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(30) NOT NULL,
activo BOOLEAN NOT NULL
);

CREATE TABLE producto(
id_prod int PRIMARY KEY AUTO_INCREMENT,
id_cat INT,
nombre VARCHAR(30) NOT NULL,
precio DECIMAL(5,2) NOT NULL,
FOREIGN KEY (id_cat) REFERENCES categoria(id_cat)
);

insert into categoria values
	(NULL, "vestidos", TRUE),
	(NULL, "zapatillas", TRUE),
	(NULL, "polos", FALSE),
	(NULL, "pantalones", FALSE),
	(NULL, "short", TRUE),
	(NULL, "zapatos", TRUE);
    
SELECT * FROM categoria;