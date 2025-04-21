<<<<<<< HEAD
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
=======
# 📊 Projeto: Controle de Perdas na Colheita da Cana-de-Açúcar

## 🌱 Contexto
A colheita da cana-de-açúcar, especialmente a mecanizada, pode gerar perdas significativas — chegando a até 15% da produção. Este sistema foi desenvolvido para auxiliar produtores e gestores do agronegócio a registrar, calcular e acompanhar as perdas durante a colheita, permitindo uma análise mais precisa e ações corretivas.

## 🎯 Objetivo
Criar uma aplicação em Python para:
- Calcular a perda percentual entre a produção estimada e a efetivamente colhida.
- Registrar os dados por talhão.
- Armazenar os registros em arquivos `.json` e `.txt`.
- Possibilitar entrada interativa dos dados via terminal.

## 🛠️ Tecnologias e conceitos aplicados
- Python 3.13
- Funções com passagem de parâmetros
- Estruturas de dados: listas, dicionários
- Manipulação de arquivos `.txt` e `.json`
- Interface interativa via terminal (input do usuário)

## ▶️ Como executar o projeto
1. Certifique-se de ter Python instalado (3.10+).
2. Faça o download/clonagem do projeto.
3. Execute o script `main.py`:
```bash
python main.py
```
4. Siga o menu interativo para registrar os dados dos talhões.
5. Os arquivos `dados_colheita.json` e `dados_colheita.txt` serão gerados na mesma pasta.

## 🧪 Exemplo de saída em JSON
```json
[
  {
    "talhao": "Talhão 1",
    "estimada": 100,
    "colhida": 85,
    "perda_percentual": 15.0
  }
]
```

## 👨‍💻 Autores
- Tiago Alves Cordeiro - RM561791
- Edson Henrique Felix Batista - RM566321
- Matheus Parra - RM561907

---

📚 Projeto desenvolvido para a disciplina de **Gestão do Agronegócio em Python** (Cap. 3 ao 6) | FIAP 2025
>>>>>>> 7e17a7a65a3fa1ed8a386e06f6e5845caf75e188
