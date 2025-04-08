-- Criação da tabela Sensor
CREATE TABLE Sensor (
    ID_Sensor INT PRIMARY KEY,
    Tipo VARCHAR(50),
    Unidade_Medida VARCHAR(20),
    Localizacao VARCHAR(100)
);

-- Criação da tabela Cultura
CREATE TABLE Cultura (
    ID_Cultura INT PRIMARY KEY,
    Nome VARCHAR(100),
    Tipo VARCHAR(50),
    Ciclo_Cultivo VARCHAR(50)
);

-- Criação da tabela Plantacao
CREATE TABLE Plantacao (
    ID_Plantacao INT PRIMARY KEY,
    Localizacao VARCHAR(100),
    Area DOUBLE,
    ID_Cultura INT,
    FOREIGN KEY (ID_Cultura) REFERENCES Cultura(ID_Cultura)
);

-- Criação da tabela Leitura
CREATE TABLE Leitura (
    ID_Leitura INT PRIMARY KEY,
    DataHora DATETIME,
    Valor DOUBLE,
    ID_Sensor INT,
    FOREIGN KEY (ID_Sensor) REFERENCES Sensor(ID_Sensor)
);

-- Criação da tabela AjusteAplicacao
CREATE TABLE AjusteAplicacao (
    ID_Ajuste INT PRIMARY KEY,
    DataHora DATETIME,
    Tipo_Ajuste VARCHAR(50),
    Quantidade DOUBLE,
    ID_Plantacao INT,
    FOREIGN KEY (ID_Plantacao) REFERENCES Plantacao(ID_Plantacao)
);
