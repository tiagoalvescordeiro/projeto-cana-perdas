# FarmTech Solutions – Modelagem de Banco de Dados

## 🌱 Projeto: Gestão Inteligente da Agricultura

Este projeto faz parte do desenvolvimento da startup fictícia **FarmTech Solutions**, voltada à Agricultura Digital com uso intensivo de sensores para monitoramento de plantações.

### 📘 Escopo

Modelar um banco de dados relacional capaz de armazenar e analisar os dados coletados por sensores instalados em plantações.

### 🌾 Sensores Utilizados

- **S1**: Sensor de umidade
- **S2**: Sensor de pH
- **S3**: Sensor de nutrientes (Fósforo e Potássio – NPK)

### 🧩 Objetivos da Modelagem

- Acompanhar a variação dos níveis de umidade, pH e nutrientes no solo.
- Registrar e otimizar os ajustes de aplicação de água e vitaminas.
- Analisar os dados ao longo do tempo e por tipo de cultura.
- Permitir previsões com base em dados históricos.

---

## 🧱 Modelo Entidade Relacionamento (MER)

### Entidades:

- **Sensor**: identifica tipo, unidade e localização.
- **Leitura**: registra valor captado, data e hora.
- **Cultura**: tipo de cultivo associado à plantação.
- **Plantação**: onde ocorre o cultivo e aplicação.
- **AjusteAplicacao**: histórico de correções feitas na lavoura.

### Relacionamentos:

- Um sensor realiza várias leituras (`1:N`)
- Uma plantação pode ter várias leituras e ajustes (`1:N`)
- Uma cultura pode estar associada a várias plantações (`1:N`)

---

## 🗃️ Estrutura dos Arquivos

| Arquivo                    | Descrição                                     |
|---------------------------|-----------------------------------------------|
| `modelo_agro.sql`         | Script SQL com criação das tabelas e relações |
| `modelo_agro.xml`         | Modelo do SQL Developer Data Modeler          |
| `modelo_agro.png`         | Imagem visual do DER                          |
| `README.md`               | Documentação geral                            |

---

## 🧠 Tecnologias Utilizadas

- Oracle SQL Developer Data Modeler
- Linguagem SQL (DDL)
- RStudio + GitHub (gestão de versionamento)
- Markdown (.md)

---

## 🎓 FIAP – Curso de Inteligência Artificial  
**Fase 2 — Capítulos 10 a 12**  
