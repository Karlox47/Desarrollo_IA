CREATE DATABASE IF NOT EXISTS app_ia;
USE app_ia;

CREATE TABLE usuarios (
    idusuarios INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    contraseña VARCHAR(255) NOT null);
   
/*INSERT INTO usuarios (nombres, apellidos, correo, contraseña) VALUES
    ('José Carlos', 'Rivero Mamani', 'resilence@gmail.com', '334433a'),
    ('Angie Dianne', 'Mallqui Campó', '123123@gmail.com', '998899'),
    ('Ashley', 'Velásquez  Oporto', 'Ssssnie@gmail.com', '112211'),
    ('Sanji', 'Vinsmoke', '66wrw@gmail.com', '665566');*/
   
   
-- Muestras
 
select * from usuarios;

show tables;