mysql -uroot

CREATE USER 'duo'@'localhost' IDENTIFIED BY '123';

CREATE DATABASE tiendalibros;

USE tiendalibros;

CREATE TABLE libros(
    -> id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -> nombre VARCHAR(60),
    -> autor VARCHAR(60),
    -> categoria VARCHAR(30),
    -> precio FLOAT,
    -> editorial VARCHAR(40)
    -> stock INT UNSIGNED
    -> ventas INT UNSIGNED);

CREATE TABLE clientes(
    -> id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -> nombres VARCHAR(40),
    -> apellidos VARCHAR(40),
    -> tarjeta VARCHAR(19),
    -> correo VARCHAR(60),
    -> contra VARCHAR(15),
    -> numtel VARCHAR(15),
    -> direccion VARCHAR(80));

CREATE TABLE mensajeria(
    -> id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -> nombre VARCHAR(40),
    -> costo FLOAT);

CREATE TABLE carrito(
    -> id_libro INT UNSIGNED NOT NULL,
    -> FOREIGN KEY (id_libro) REFERENCES libros(id),
    -> id_cliente INT UNSIGNED NOT NULL,
    -> FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    -> estatus VARCHAR(20),
    -> met_pago VARCHAR(25),
    -> cantidad INT UNSIGNED,
    -> fecha_ped DATE,
    -> importe_t FLOAT,
    -> id_mensj INT UNSIGNED NOT NULL,
    -> FOREIGN KEY (id_mensj) REFERENCES mensajeria(id)
    -> modo_mensj VARCHAR(25));

CREATE TABLE historial(
    -> id_libro INT UNSIGNED NOT NULL,
    -> FOREIGN KEY (id_libro) REFERENCES libros(id),
    -> id_cliente INT UNSIGNED NOT NULL,
    -> FOREIGN KEY (id_cliente) REFERENCES clientes(id),
    -> fecha_ped DATE,
    -> fecha_rec DATE
    -> costo FLOAT);

GRANT ALL PRIVILEGES ON tiendalibros.* TO 'duo'@'localhost';