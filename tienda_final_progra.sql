use b0swpdxifjydkzpaud8j;

CREATE TABLE categoria(
id_cat INT PRIMARY KEY AUTO_INCREMENT,
nombre_cat VARCHAR(20) NOT NULL,
estado BOOLEAN DEFAULT True
);

CREATE TABLE producto(
id_prod INT PRIMARY KEY AUTO_INCREMENT,
id_cat INT NOT NULL,
nombre_prod VARCHAR(50) NOT NULL,
precio_prod DECIMAL(5,2) NOT NULL,
stock INT NOT NULL,
estado BOOLEAN NOT NULL,
FOREIGN KEY (id_cat) REFERENCES categoria(id_cat)
);

CREATE TABLE promociones(
codigo_desc VARCHAR(20) PRIMARY KEY,
fec_inicio DATETIME DEFAULT NOW(),
fec_final DATE NOT NULL,
estado BOOLEAN
);

CREATE TABLE venta(
num_venta INT PRIMARY KEY AUTO_INCREMENT,
fec_venta DATETIME DEFAULT NOW(),
codigo_desc VARCHAR(20),
descuento decimal(8,2) default 0,
total decimal(8,2),
FOREIGN KEY (codigo_desc) REFERENCES promociones(codigo_desc)
);

CREATE TABLE detalle_venta(
num_venta INT NOT NULL,
id_prod INT NOT NULL,
cantidad INT NOT NULL,
subtotal decimal(7,2),
FOREIGN KEY (num_venta) REFERENCES venta(num_venta),
FOREIGN KEY (id_prod) REFERENCES producto(id_prod)
);

INSERT INTO categoria(nombre_cat) VALUES('vestidos');

select * from categoria;

-- drop table producto;
-- drop table categoria;
