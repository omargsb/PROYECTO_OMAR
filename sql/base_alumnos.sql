CREATE DATABASE base_alumnos;

USE base_alumnos;

CREATE TABLE datos(
    matricula varchar(14) NOT NULL PRIMARY KEY,
    nombre varchar(10) NOT NULL,
    a_paterno varchar(15) NOT NULL,
    a_materno varchar(15) NOT NULL,
    calle varchar(40) NOT NULL,
    numero varchar(4) NOT NULL,
    colonia varchar(40) NOT NULL,
    municipio varchar(20) NOT NULL,
    estado varchar(20) NOT NULL,
    cp varchar(5) NOT NULL,
    email varchar(30) NOT NULL,
    password varchar (16) NOT NULL
   )ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO datos (matricula, nombre, a_paterno, a_materno, calle, numero, colonia, municipio, estado, cp, email, password)
VALUES ('10010','JUAN','LOPEZ','RAMIREZ','AV, COLOSIO','100','LAS LOMAS','ACTOPAN','HIDALGO','42667','jlopez@gmail.com','Qwerty12'),
       ('10011','MARIA','NICOLASA','ORTIZ','CIPRES','15','LOS CHAVARRIAS','FCO. I MADERO','HIDALGO','42660','mnicol@gmail.com','Asdfgh12');

SHOW TABLES;

SELECT * FROM datos;

DESCRIBE datos;

SELECT "Creando un usuario y asignandolo a la base de datos" as "Mensaje";
CREATE USER 'omar'@'localhost' IDENTIFIED BY 'omar.2018';
GRANT ALL PRIVILEGES ON base_alumnos.* TO 'omar'@'localhost';
-- GRANT ALL PRIVILEGES ON base_demo.* TO kuorra@'%' IDENTIFIED BY 'kuorra.remote';

FLUSH PRIVILEGES;
