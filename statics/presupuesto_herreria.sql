CREATE DATABASE presupuesto_herreria

CREATE table datos_clientes (
    cuilt_cliente VARCHAR(13) NOT NULL PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    direccion VARCHAR(45) NOT NULL,
    ciudad VARCHAR(45) NOT NULL,
    telefono VARCHAR(45) NOT NULL
);

CREATE table ubicacion_trabajo (
    id_ubicacion INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    domicilio VARCHAR(60) NOT NULL,
    ciudad VARCHAR(45)
);

CREATE TABLE presupuesto (
    id_presupuesto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_presupuesto DATE NOT NULL,
    fk_ubicacion_trabajo INT NOT NULL,
    fk_datos_clientes VARCHAR(13) NOT NULL,
    tipo_calculo ENUM('PORCENTAJE', 'POR_HORA') NOT NULL,
    costo_porcentaje DECIMAL(5, 2) NULL,
    costo_hora_trabajo DECIMAL(10, 2) NULL,
    duracion_horas DECIMAL(5, 2) NULL,
    FOREIGN KEY (fk_ubicacion_trabajo) REFERENCES ubicacion_trabajo (id_ubicacion) ON DELETE CASCADE,
    FOREIGN KEY (fk_datos_clientes) REFERENCES datos_clientes (cuilt_cliente) ON DELETE CASCADE
);

CREATE Table proveedor_materiales (
    id_proveedor_materiales INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    rubro VARCHAR(45) NOT NULL,
    telefono VARCHAR(45) NOT NULL
);

CREATE TABLE materiales (
    id_material INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(40) NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    fk_proveedor_materiales INT NOT NULL,
    FOREIGN KEY (fk_proveedor_materiales) REFERENCES proveedor_materiales (id_proveedor_materiales) ON DELETE CASCADE
);

CREATE TABLE detalle_presupuesto (
    id_detalle INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fk_presupuesto int NOT NULL,
    fk_materiales int NOT NULL,
    cantidad INT NOT NULL,
    Foreign Key (fk_presupuesto) REFERENCES presupuesto (id_presupuesto) ON DELETE CASCADE,
    Foreign Key (fk_materiales) REFERENCES materiales (id_material) ON DELETE CASCADE
);