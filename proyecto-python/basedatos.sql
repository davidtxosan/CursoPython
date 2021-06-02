CREATE DATABASE IF NOT EXISTS  master_python;
use master_python;

CREATE  TABLE usuarios(
id          int(10) auto_increment not null,
nombre      varchar(100),
apellidos   varchar(100),
email       VARCHAR(100) not null,
password    VARCHAR(100) not NULL,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY (id),
CONSTRAINT uq_email UNIQUE (email)

)ENGINE=InnoDb;

CREATE TABLE notas(
    id          int(25) AUTO_INCREMENT  NOT  NULL ,
    usuario_id  int(25) not NULL ,
    titulo      varchar(100) not NULL ,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    


)ENGINE=InnoDb;