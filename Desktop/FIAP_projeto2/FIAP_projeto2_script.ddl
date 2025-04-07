-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-04-07 09:02:37 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE Fazenda 
    ( 
     ID_Fazenda  INTEGER  NOT NULL , 
     Nome        VARCHAR2 (100)  NOT NULL , 
     Localizacao VARCHAR2 (100)  NOT NULL 
    ) 
;

ALTER TABLE Fazenda 
    ADD CONSTRAINT Fazenda_PK PRIMARY KEY ( ID_Fazenda ) ;

CREATE TABLE Leitura 
    ( 
     ID_Leitura     INTEGER  NOT NULL , 
     ID_Sensor      INTEGER  NOT NULL , 
     Data_Hora      TIMESTAMP  NOT NULL , 
     Valor_Coletado NUMBER  NOT NULL 
    ) 
;

ALTER TABLE Leitura 
    ADD CONSTRAINT Leitura_Sensor_PK PRIMARY KEY ( ID_Leitura ) ;

CREATE TABLE Sensor 
    ( 
     ID_Sensor   INTEGER  NOT NULL , 
     Tipo_Sensor VARCHAR2 (50)  NOT NULL , 
     Descricao   VARCHAR2 (100) , 
     ID_Fazenda  INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Sensor 
    ADD CONSTRAINT Sensor_PK PRIMARY KEY ( ID_Sensor ) ;

ALTER TABLE Leitura 
    ADD CONSTRAINT Leitura_Sensor_FK FOREIGN KEY 
    ( 
     ID_Sensor
    ) 
    REFERENCES Sensor 
    ( 
     ID_Sensor
    ) 
;

CREATE SEQUENCE Leitura_ID_Leitura_SEQ 
START WITH 1 
    NOCACHE 
    ORDER ;

CREATE OR REPLACE TRIGGER Leitura_ID_Leitura_TRG 
BEFORE INSERT ON Leitura 
FOR EACH ROW 
WHEN (NEW.ID_Leitura IS NULL) 
BEGIN 
    :NEW.ID_Leitura := Leitura_ID_Leitura_SEQ.NEXTVAL; 
END;
/



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              4
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           1
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          1
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
